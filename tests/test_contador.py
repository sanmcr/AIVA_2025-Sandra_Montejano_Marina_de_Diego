import unittest
import cv2
import os
import xml.etree.ElementTree as ET
from src.python.mockup import contar_celulas, generar_xml, mostrar_bounding_boxes

class TestContadorGlobulos(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """ Configuración inicial global para las pruebas """
        cls.imagen_path = "img/JPGImages/BloodImage_00000.jpg"
        cls.xml_output_path = "img/annotations/resultado_test.xml"

    def test_carga_imagen(self):
        """ Verifica que la imagen de prueba existe y se puede cargar correctamente. """
        self.assertTrue(os.path.exists(self.imagen_path), "La imagen de prueba no existe.")
        
        imagen = cv2.imread(self.imagen_path, cv2.IMREAD_GRAYSCALE)  # Cargar en escala de grises
        self.assertIsNotNone(imagen, "No se pudo cargar la imagen. Verifica la ruta o el formato.")

    def test_contar_celulas(self):
        """ Comprueba que el sistema detecta células en la imagen de prueba. """
        imagen = cv2.imread(self.imagen_path, cv2.IMREAD_GRAYSCALE)
        self.assertIsNotNone(imagen, "La imagen no se pudo cargar correctamente.")

        num_celulas, bboxes = contar_celulas(imagen)
        self.assertGreater(num_celulas, 0, "Debe detectar al menos una célula.")
        self.assertIsInstance(bboxes, list, "Debe devolver una lista de bounding boxes.")

    def test_generacion_xml(self):
        """ Verifica que el XML generado contiene la estructura correcta. """
        bboxes = [(10, 20, 30, 40), (50, 60, 70, 80)]
        generar_xml(bboxes, self.xml_output_path)

        self.assertTrue(os.path.exists(self.xml_output_path), "El XML no se generó correctamente.")

        # Validar estructura del XML
        tree = ET.parse(self.xml_output_path)
        root = tree.getroot()
        self.assertEqual(root.tag, "celulas", "El XML debe contener una etiqueta <celulas>.")

        # Validar cantidad de células en XML
        celulas = root.findall("celula")
        self.assertEqual(len(celulas), len(bboxes), "El número de células en el XML no coincide con las detectadas.")

        # Imprimir la ruta del XML generado para depuración
        print(f"XML generado en: {self.xml_output_path}")

        # Borrar el archivo después de la prueba
        os.remove(self.xml_output_path)

if __name__ == '__main__':
    unittest.main()
