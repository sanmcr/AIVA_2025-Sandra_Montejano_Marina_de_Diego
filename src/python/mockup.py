import cv2
import xml.etree.ElementTree as ET
import os

def contar_celulas(imagen):
    """ Simulación de segmentación de células """
    if imagen is None:
        raise ValueError("No se pudo cargar la imagen correctamente.")

    bounding_boxes = [(10, 20, 30, 40), (50, 60, 70, 80)]
    return len(bounding_boxes), bounding_boxes

def generar_xml(bboxes, xml_output_path="img/annotations/resultado_test.xml"):
    """ Genera un XML con la ubicación de las células detectadas """

    # Garantizar que el directorio existe antes de escribir el XML
    os.makedirs(os.path.dirname(xml_output_path), exist_ok=True)

    root = ET.Element("celulas")
    for (x, y, w, h) in bboxes:
        ET.SubElement(root, "celula", x=str(x), y=str(y), width=str(w), height=str(h))

    tree = ET.ElementTree(root)
    tree.write(xml_output_path)
    
    print(f"✅ Archivo XML generado correctamente en: {xml_output_path}")  # 🔍 DEBUG PRINT

def mostrar_bounding_boxes(imagen, bboxes):
    """ Dibuja los bounding boxes en la imagen y la muestra si no está en GitHub Actions """
    for (x, y, w, h) in bboxes:
        cv2.rectangle(imagen, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    if "GITHUB_ACTIONS" not in os.environ:  # Evitar errores en CI/CD
        cv2.imshow("Detección de Células", imagen)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

if __name__ == "__main__":
    imagen_path = "img/JPGImages/BloodImage_00000.jpg"

    if not os.path.exists(imagen_path):
        print("❌ Error: La imagen de prueba no existe.")
    else:
        imagen = cv2.imread(imagen_path, cv2.IMREAD_GRAYSCALE)
        if imagen is None:
            print("❌ Error: No se pudo cargar la imagen.")
        else:
            num_celulas, bboxes = contar_celulas(imagen)
            print(f"🔍 Células detectadas: {num_celulas}")
            generar_xml(bboxes)
