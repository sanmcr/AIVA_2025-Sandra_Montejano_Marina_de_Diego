import os
import cv2
import xml.etree.ElementTree as ET

def contar_celulas(imagen):
    """ Simulación de segmentación de células """
    if imagen is None:
        raise ValueError("No se pudo cargar la imagen correctamente.")

    # Simulación de detección de células
    bounding_boxes = [(10, 20, 30, 40), (50, 60, 70, 80)]
    return len(bounding_boxes), bounding_boxes

def generar_xml(bboxes, xml_output_path="img/annotations/resultado.xml"):
    """ Genera un XML con la ubicación de las células detectadas """

    # Obtener ruta absoluta para depuración
    abs_path = os.path.abspath(xml_output_path)
    print(f"Intentando generar XML en: {abs_path}")  # Depuración

    root = ET.Element("celulas")
    for (x, y, w, h) in bboxes:
        ET.SubElement(root, "celula", x=str(x), y=str(y), width=str(w), height=str(h))

    # Asegurar que el directorio de salida existe y tiene permisos de escritura
    output_dir = os.path.dirname(xml_output_path)
    os.makedirs(output_dir, exist_ok=True)
    os.chmod(output_dir, 0o777)  # Dar permisos completos

    # Guardar el XML
    tree = ET.ElementTree(root)
    tree.write(xml_output_path)

    # Confirmación
    print(f"Archivo XML generado en: {abs_path}")

def mostrar_bounding_boxes(imagen, bboxes):
    """ Dibuja los bounding boxes en la imagen y la muestra si no está en GitHub Actions """
    for (x, y, w, h) in bboxes:
        cv2.rectangle(imagen, (x, y), (x + w, y + h), (0, 255, 0), 2)

    if "GITHUB_ACTIONS" not in os.environ:  # Solo muestra la imagen si no está en GitHub Actions
        cv2.imshow("Detección de Células", imagen)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

if __name__ == "__main__":
    imagen_path = "img/JPGImages/BloodImage_00000.jpg"

    if not os.path.exists(imagen_path):
        print("Error: La imagen de prueba no existe.")
    else:
        imagen = cv2.imread(imagen_path, cv2.IMREAD_GRAYSCALE)
        if imagen is None:
            print("Error: No se pudo cargar la imagen.")
        else:
            num_celulas, bboxes = contar_celulas(imagen)
            print(f"Células detectadas: {num_celulas}")
            generar_xml(bboxes)
            mostrar_bounding_boxes(imagen, bboxes)  # Eliminé `mostrar=True` ya que no existe en la función
