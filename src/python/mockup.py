import cv2
import xml.etree.ElementTree as ET
import os

def contar_celulas(imagen):
    """ Simulación de segmentación de células """
    bounding_boxes = [(10, 20, 30, 40), (50, 60, 70, 80)]  # Simulación
    return len(bounding_boxes), bounding_boxes

def generar_xml(bboxes, xml_output_path="imagenes_prueba/annotations/resultado.xml"):
    """ Genera un XML con la ubicación de las células """
    root = ET.Element("celulas")
    for (x, y, w, h) in bboxes:
        ET.SubElement(root, "celula", x=str(x), y=str(y), width=str(w), height=str(h))

    tree = ET.ElementTree(root)
    os.makedirs(os.path.dirname(xml_output_path), exist_ok=True)
    tree.write(xml_output_path)
    print(f"Archivo XML generado: {xml_output_path}")

def mostrar_bounding_boxes(imagen, bboxes):
    """ Dibuja los bounding boxes en la imagen y la muestra """
    for (x, y, w, h) in bboxes:
        cv2.rectangle(imagen, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
    cv2.imshow("Detección de Células", imagen)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    imagen_path = "imagenes_prueba/JPGImages/BloodImage_00000.jpg"  # Usa una imagen existente
    if not os.path.exists(imagen_path):
        print("Error: La imagen de prueba no existe.")
    else:
        imagen = cv2.imread(imagen_path)
        num_celulas, bboxes = contar_celulas(imagen)
        generar_xml(bboxes)
        mostrar_bounding_boxes(imagen, bboxes)

