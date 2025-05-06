import os
from typing import List

import cv2
import numpy as np
from scipy import ndimage
from skimage.feature import peak_local_max
from skimage.segmentation import watershed
from skimage.measure import label
from skimage.morphology import disk
import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom


class Image:
    def __init__(self, path: str, data: np.ndarray):
        self.path = path
        self.data = data
        self.width = data.shape[1]
        self.height = data.shape[0]
        self.channels = data.shape[2]

class Erythrocyte:
    def __init__(self, xmin: int, xmax: int, ymin: int, ymax: int):
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax

class AppCore:
    def getImagePaths(self, imagePathsList: List[str]) -> List[str]:
        return imagePathsList

    def saveResults(self, savingPath: str, xmlGenerated: str, originalImage: Image) -> None:
        image_name = os.path.basename(originalImage.path).split('.')[0]
        complete_path = savingPath + '/' + image_name + '.xml'

        with open(complete_path, 'w', encoding='utf-8') as file:
            file.write(xmlGenerated)

    def saveImage(self, savingPath: str, originalImage: Image, cellsList: List[Erythrocyte]) -> None:
        image = originalImage.data
        image_name = os.path.basename(originalImage.path).split('.')[0]
        complete_path = savingPath + '/' + image_name + '_processed.png'
        for cell in cellsList:
            cv2.rectangle(image, (cell.xmin,cell.ymin), (cell.xmax,cell.ymax), (255,0,0), 2)

        success = cv2.imwrite(complete_path, image)
        print(success)

class ImageManager:
    def __init__(self, imagePath: str):
        self.imagePath = imagePath

    def readImage(self) -> Image:
        image_data = cv2.imread(self.imagePath)
        return Image(self.imagePath, image_data)

    def validateImage(self, imageToValidate: Image) -> bool:
        imageWidth = imageToValidate.width
        imageHeight = imageToValidate.height
        imageChannels = imageToValidate.channels

        if imageWidth == 640 and imageHeight == 480 and imageChannels == 3:
            return True
        else:
            return False

class ImageProcessor:

    def processImage(self, imageToProcess: Image) -> List[Erythrocyte]:
        img = imageToProcess.data
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
        gray_clahe = clahe.apply(gray)

        _, mask = cv2.threshold(gray_clahe, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9, 9))
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        lower_purple = np.array([110, 50, 50])
        upper_purple = np.array([150, 255, 255])
        purple_mask = cv2.inRange(hsv, lower_purple, upper_purple)
        purple_mask = cv2.dilate(purple_mask, np.ones((3, 3), np.uint8), iterations=2)
        mask[purple_mask > 0] = 0

        dist = cv2.distanceTransform(mask, cv2.DIST_L2, 5)
        dist = cv2.GaussianBlur(dist, (5, 5), 1.0)

        labels_connected = label(mask).astype(np.int32)

        coordinates = peak_local_max(
            dist,
            min_distance=10,
            threshold_abs=3.5,
            footprint=disk(10),
            labels=labels_connected
        )

        markers = np.zeros_like(gray, dtype=np.int32)
        for i, (r, c) in enumerate(coordinates, start=1):
            markers[r, c] = i

        labels_ws = watershed(-dist, markers, mask=mask.astype(bool))

        cellsList = []
        for label_id in np.unique(labels_ws):
            if label_id == 0:
                continue
            mask_label = (labels_ws == label_id).astype("uint8") * 255
            if cv2.countNonZero(mask_label) < 100:
                continue

            cnts, _ = cv2.findContours(mask_label, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            if cnts:
                x, y, w, h = cv2.boundingRect(cnts[0])
                cell = Erythrocyte(x, x + w, y, y + h)
                cellsList.append(cell)

        return cellsList

    def countCells(self, cellsList: List[Erythrocyte]) -> int:
        return len(cellsList)

class ResultsProcessor:
    def generateXML(self, originalImage: Image, cellsList: List[Erythrocyte]) -> str:
        image_name = os.path.basename(originalImage.path)

        annotation = ET.Element("annotation", verified="no")

        ET.SubElement(annotation, "folder").text = "RBC"
        ET.SubElement(annotation, "filename").text = image_name.split('.')[0]
        ET.SubElement(annotation, "path").text = originalImage.path + '/' + image_name

        source = ET.SubElement(annotation, "source")
        ET.SubElement(source, "database").text = "Unknown"

        size = ET.SubElement(annotation, "size")
        ET.SubElement(size, "width").text = "640"
        ET.SubElement(size, "height").text = "480"
        ET.SubElement(size, "depth").text = "3"
        ET.SubElement(annotation, "segmented").text = "0"

        for cell in cellsList:
            xmin = cell.xmin
            ymin = cell.ymin
            xmax = cell.xmax
            ymax = cell.ymax

            obj = ET.SubElement(annotation, "object")
            ET.SubElement(obj, "name").text = "RBC"
            ET.SubElement(obj, "pose").text = "Unspecified"
            ET.SubElement(obj, "truncated").text = "0"
            ET.SubElement(obj, "difficult").text = "0"

            bbox = ET.SubElement(obj, "bndbox")
            ET.SubElement(bbox, "xmin").text = str(xmin)
            ET.SubElement(bbox, "ymin").text = str(ymin)
            ET.SubElement(bbox, "xmax").text = str(xmax)
            ET.SubElement(bbox, "ymax").text = str(ymax)

        xml_result = ET.tostring(annotation, encoding="utf-8")
        reparsed = minidom.parseString(xml_result)
        pretty_xml = reparsed.toprettyxml(indent="  ")

        return pretty_xml

class JavaIntegrator:
    def __init__(self):
        self.requests = []
        self.results = []

    def receiveRequest(self, request_data: list[str]) -> None:
        self.requests.extend(request_data)
        print("[JavaIntegrator] Solicitudes recibidas desde Java:")
        for req in request_data:
            print(f"  - {req}")

    def sendResults(self, result_data: list[str]) -> None:
        self.results.extend(result_data)
        print("[JavaIntegrator] Resultados enviados a Java:")
        for res in result_data:
            print(f"  - {res}")

