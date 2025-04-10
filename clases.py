from typing import List
import numpy as np
import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom
import cv2
import os

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

    def processImage(self,  imageToProcess: Image) -> List[Erythrocyte]:
        image = imageToProcess.data
        cellsList = []

        # 1. Preprocessing
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
        enhanced = clahe.apply(gray)
        denoised = cv2.bilateralFilter(enhanced, d=9, sigmaColor=75, sigmaSpace=75)

        # 2. Binarize
        _, binary = cv2.threshold(denoised, 150, 255, cv2.THRESH_BINARY_INV)

        # 3. Morphological operations
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
        opened = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel, iterations=2)
        closed = cv2.morphologyEx(opened, cv2.MORPH_CLOSE, kernel, iterations=3)

        # 4. Watershed
        dist_transform = cv2.distanceTransform(closed, cv2.DIST_L2, 5)
        dist_8bit = cv2.normalize(dist_transform, None, 0, 255,
                                  cv2.NORM_MINMAX).astype(np.uint8)


        # Watershed threshold
        _, sure_fg = cv2.threshold(dist_8bit, 0, 100,
                                   cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        sure_fg = np.uint8(sure_fg)

        sure_bg = cv2.dilate(closed, kernel, iterations=2)
        unknown = cv2.subtract(sure_bg, sure_fg)

        # markers
        ret, markers = cv2.connectedComponents(sure_fg)
        markers += 1
        markers[unknown == 255] = 0

        # apply watershed
        markers = cv2.watershed(cv2.cvtColor(denoised, cv2.COLOR_GRAY2BGR), markers)

        # 5. Post-processing and bounding boxes
        #min_area = 50
        #max_area = 300
        min_circularity = 0.6

        for marker in np.unique(markers):
            if marker > 1:
                mask = np.zeros_like(markers, dtype=np.uint8)
                mask[markers == marker] = 255

                contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL,
                                               cv2.CHAIN_APPROX_SIMPLE)
                if contours:
                    cnt = contours[0]
                    area = cv2.contourArea(cnt)

                    #if area < min_area or area > max_area:
                    #    continue

                    perimeter = cv2.arcLength(cnt, True)
                    if perimeter == 0:
                        continue

                    circularity = 4 * np.pi * area / (perimeter ** 2)
                    if circularity < min_circularity:
                        continue

                    # Calcular bounding box
                    x, y, w, h = cv2.boundingRect(cnt)
                    erytrocyte = Erythrocyte(x, x + w, y, y + h)
                    cellsList.append(erytrocyte)

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

