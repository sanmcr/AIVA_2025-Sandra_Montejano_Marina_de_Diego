import unittest
import cv2
import os
import xml.etree.ElementTree as ET
from src.python.mockup import contar_celulas, generar_xml, mostrar_bounding_boxes

class TestContadorGlobulos(unittest.TestCase):

    def setUp(self):
        """ Configuración inicial: Define rutas de prueba. """
        self.imagen_path = "imag/JPGImages/BloodImage_00000.jpg"
        self.xml_output_path = "img/annotations/resultado_test.xml"

    def test_carga_imagen(self):
        """ Verifica que la imagen de prueba existe y se puede cargar. """
        self.assertTrue(os.path.exists(self.imagen_path), "La imagen de prueba no existe.")
        imagen = cv2.imread(self.imagen_path, 0)  # Cargar en escala de grises
        self.assertIsNotNone(imagen, "No se pudo cargar la imagen.")

    def test_contar_celulas(self):
        """ Comprueba que el sistema detecta células en la imagen de prueba. """
        imagen = cv2.imread(self.imagen_path, 0)
        num_celulas, bboxes = contar_celulas(imagen)
        self.assertGreater(num_celulas, 0, "Debe detectar al menos una célula.")
        self.assertIsInstance(bboxes, list, "Debe devolver una lista de bounding boxes.")

    def test_generacion_xml(self):
        """ Verifica que el XML generado contiene la estructura correcta. """
        bboxes = [(10, 20, 30, 40), (50, 60, 70, 80)]
        generar_xml(bboxes, self.xml_output_path)

        # Comprobar que el archivo se generó
        self.assertTrue(os.path.exists(self.xml_output_path), "El XML no se generó correctamente.")

        # Validar estructura del XML
        tree = ET.parse(self.xml_output_path)
        root = tree.getroot()
        self.assertEqual(root.tag, "celulas", "El XML debe contener una etiqueta <celulas>.")

        # Validar contenido de las células detectadas
        celulas = root.findall("celula")
        self.assertEqual(len(celulas), len(bboxes), "El número de células en el XML no coincide con las detectadas.")

        # Borrar el archivo después de la prueba
        os.remove(self.xml_output_path)

    def test_visualizacion_bounding_boxes(self):
        """ Comprueba que el método para mostrar bounding boxes no falla. """
        imagen = cv2.imread(self.imagen_path)
        _, bboxes = contar_celulas(imagen)

        try:
            mostrar_bounding_boxes(imagen, bboxes)
            resultado = True
        except Exception as e:
            resultado = False
            print("Error al mostrar bounding boxes:", e)

        self.assertTrue(resultado, "La función de visualización falló.")

if __name__ == '__main__':
    unittest.main()

