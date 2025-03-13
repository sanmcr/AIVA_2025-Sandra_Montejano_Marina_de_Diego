import numpy as np
import cv2
import xml.etree.ElementTree as ET
import random
import os


def generar_imagen_mock(variar_celulas=True, agregar_ruido=False):
    """Genera una imagen simulada con células como círculos blancos."""
    imagen_mock = np.zeros((480, 640, 3), dtype=np.uint8)

    num_celulas = random.randint(5, 15) if variar_celulas else 10
    coordenadas_celulas = []

    for _ in range(num_celulas):
        x_min, y_min = np.random.randint(50, 590), np.random.randint(50, 430)
        x_max, y_max = x_min + np.random.randint(10, 50), y_min + np.random.randint(10, 50)
        cv2.rectangle(imagen_mock, (x_min, y_min), (x_max, y_max), (255, 255, 255), -1)
        coordenadas_celulas.append((x_min, y_min, x_max, y_max))

    if agregar_ruido:
        ruido = np.random.randint(0, 50, imagen_mock.shape, dtype=np.uint8)
        imagen_mock = cv2.add(imagen_mock, ruido)

    return imagen_mock, coordenadas_celulas


def contar_celulas_mock(imagen, coordenadas_celulas):
    """Cuenta el número de células en la imagen generada."""
    if imagen is None:
        raise ValueError("Imagen inválida proporcionada")
    return len(coordenadas_celulas)


def generar_xml_mock(detecciones, nombre_archivo="resultado.xml"):
    """Genera un XML con los datos de las células detectadas en el formato VOC Pascal."""
    annotation = ET.Element("annotation", verified="no")

    ET.SubElement(annotation, "folder").text = "RBC"
    ET.SubElement(annotation, "filename").text = "BloodImage_00206"
    ET.SubElement(annotation, "path").text = "/Users/cosmic/WBC_CLASSIFICATION_ANNO/RBC/BloodImage_00206.jpg"

    source = ET.SubElement(annotation, "source")
    ET.SubElement(source, "database").text = "Unknown"

    size = ET.SubElement(annotation, "size")
    ET.SubElement(size, "width").text = "640"
    ET.SubElement(size, "height").text = "480"
    ET.SubElement(size, "depth").text = "3"

    ET.SubElement(annotation, "segmented").text = "0"

    for celula in detecciones:
        x_min, y_min, x_max, y_max = celula
        obj = ET.SubElement(annotation, "object")
        ET.SubElement(obj, "name").text = "RBC"
        ET.SubElement(obj, "pose").text = "Unspecified"
        ET.SubElement(obj, "truncated").text = str(random.randint(0, 1))
        ET.SubElement(obj, "difficult").text = "0"

        bndbox = ET.SubElement(obj, "bndbox")
        ET.SubElement(bndbox, "xmin").text = str(x_min)
        ET.SubElement(bndbox, "ymin").text = str(y_min)
        ET.SubElement(bndbox, "xmax").text = str(x_max)
        ET.SubElement(bndbox, "ymax").text = str(y_max)

    xml_output = ET.tostring(annotation, encoding="utf-8").decode("utf-8")

    carpeta_salida = "xml_outputs"
    if not os.path.exists(carpeta_salida):
        os.makedirs(carpeta_salida)

    ruta_completa = os.path.join(carpeta_salida, nombre_archivo)

    with open(ruta_completa, "w", encoding="utf-8") as file:
        file.write(xml_output)

    print(f"XML guardado en: {os.path.abspath(ruta_completa)}")
    return ruta_completa


if __name__ == "__main__":
    img, coords = generar_imagen_mock(variar_celulas=True, agregar_ruido=True)
    xml_file = generar_xml_mock(coords)
    print(f"Se han detectado {len(coords)} células. El archivo XML está en: {xml_file}")
