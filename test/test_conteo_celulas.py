import unittest
import mockup
import xml.etree.ElementTree as ET
import os

class TestMockup(unittest.TestCase):
    def setUp(self):
        """Prepara imágenes simuladas antes de cada test"""
        self.imagen_prueba, self.coords = mockup.generar_imagen_mock(variar_celulas=True, agregar_ruido=True)
        self.imagen_invalida = None

    def test_mockup_generacion(self):
        """Verifica que el mockup genera una imagen correctamente"""
        self.assertIsNotNone(self.imagen_prueba)
        self.assertEqual(self.imagen_prueba.shape, (480, 640, 3))
        self.assertGreaterEqual(len(self.coords), 5)

    def test_mockup_conteo(self):
        """Verifica que el mockup cuenta correctamente las células"""
        conteo = mockup.contar_celulas_mock(self.imagen_prueba, self.coords)
        self.assertEqual(conteo, len(self.coords))

    def test_mockup_exportar_xml(self):
        """Simula la generación y almacenamiento de un archivo XML"""
        xml_file = mockup.generar_xml_mock(self.coords, "test_resultado.xml")
        self.assertTrue(os.path.exists(xml_file))

        with open(xml_file, "r", encoding="utf-8") as file:
            xml_content = file.read()

        root = ET.fromstring(xml_content)
        self.assertEqual(root.tag, "annotation")

if __name__ == '__main__':
    unittest.main()
