import unittest
import mockup
import xml.etree.ElementTree as ET
import os

class TestMockup(unittest.TestCase):
    def setUp(self):
        """Prepara imágenes simuladas antes de cada test"""
        self.imagen_prueba, self.coords = mockup.generar_imagen_mock(variar_celulas=True, agregar_ruido=True)
        self.imagen_invalida = None

    def test_mockup_carga_imagen(self):
        """Verifica que la imagen generada por el mockup tiene el tamaño correcto"""
        self.assertIsNotNone(self.imagen_prueba, "La imagen no se generó correctamente")
        self.assertEqual(self.imagen_prueba.shape, (480, 640, 3), "El tamaño de la imagen no es el esperado")

    def test_mockup_segmentacion(self):
        """Verifica que el mockup segmenta correctamente las células"""
        self.assertGreater(len(self.coords), 0, "No se detectaron células en la segmentación")

    def test_mockup_agregar_bounding_box(self):
        """Simula la adición manual de un bounding box"""
        coordenadas_nuevas = (100, 100, 150, 150)
        self.coords = mockup.agregar_bounding_box(self.coords, coordenadas_nuevas)
        self.assertIn(coordenadas_nuevas, self.coords, "El bounding box manual no se agregó correctamente")

    def test_mockup_eliminar_bounding_box(self):
        """Simula la eliminación manual de un bounding box"""
        if self.coords:
            bbox_a_eliminar = self.coords[0]
            self.coords = mockup.eliminar_bounding_box(self.coords, bbox_a_eliminar)
            self.assertNotIn(bbox_a_eliminar, self.coords, "El bounding box manual no se eliminó correctamente")

    def test_mockup_xml_contiene_datos_validos(self):
        """Verifica que el XML generado contenga información válida"""
        xml_file = mockup.generar_xml_mock(self.coords, "test_resultado.xml")
        self.assertTrue(os.path.exists(xml_file), "El archivo XML no se generó correctamente")

        with open(xml_file, "r", encoding="utf-8") as file:
            xml_content = file.read()

        root = ET.fromstring(xml_content)
        objects = root.findall("object")
        self.assertEqual(len(objects), len(self.coords), "El número de células en el XML no coincide con la segmentación")

    def test_mockup_exportar_resultados(self):
        """Verifica que el archivo XML exportado tenga la cantidad correcta de células"""
        xml_file = mockup.generar_xml_mock(self.coords, "test_export.xml")
        self.assertTrue(os.path.exists(xml_file), "El archivo XML de exportación no se generó correctamente")

        with open(xml_file, "r", encoding="utf-8") as file:
            xml_content = file.read()

        root = ET.fromstring(xml_content)
        self.assertEqual(root.tag, "annotation", "El XML generado no tiene la etiqueta raíz esperada")

        # Eliminar el archivo después del test
        os.remove(xml_file)
        self.assertFalse(os.path.exists(xml_file), "El archivo XML de prueba no se eliminó correctamente")

if __name__ == '__main__':
    unittest.main()
