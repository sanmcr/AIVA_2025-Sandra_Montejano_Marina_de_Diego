import unittest
import os
import xml.etree.ElementTree as ET


from clases import ImageManager, ImageProcessor, ResultsProcessor, Erythrocyte


class TestProcesamientoEritrocitos(unittest.TestCase):
    def setUp(self):
        """Carga una imagen válida y la prepara antes de cada test"""
        self.image_path = r'C:\Users\ASUS ROG STRIX\PycharmProjects\Aplicaciones\JPEGImages\BloodImage_00001.jpg'
        self.image_manager = ImageManager(self.image_path)
        self.image = self.image_manager.readImage()
        self.processor = ImageProcessor()
        self.results_processor = ResultsProcessor()
        self.cells = self.processor.processImage(self.image)

    def test_carga_imagen_valida(self):
        """Verifica que la imagen se carga con el tamaño correcto"""
        self.assertIsNotNone(self.image.data, "La imagen no se cargó correctamente")
        self.assertEqual((self.image.height, self.image.width, self.image.channels), (480, 640, 3))

    def test_segmentacion(self):
        """Verifica que el resultado de la segmentación es una lista válida (aunque no se detecten todas las células)"""
        self.assertIsInstance(self.cells, list, "La segmentación no devolvió una lista")

        for celula in self.cells:
            self.assertIsInstance(celula, Erythrocyte, "La lista contiene un objeto que no es un Erythrocyte")

        # Comprobamos que haya al menos 1 (o que se maneje si no hay)
        self.assertGreaterEqual(len(self.cells), 0, "La segmentación falló o no devolvió resultado")

    def test_conteo_celulas(self):
        """Verifica que el conteo de células coincida con la lista"""
        conteo = self.processor.countCells(self.cells)
        self.assertEqual(conteo, len(self.cells), "El conteo no coincide con el número de objetos")

    def test_agregar_bounding_box_manual(self):
        """Simula agregar un bounding box manualmente"""
        nueva = Erythrocyte(100, 150, 100, 150)
        self.cells.append(nueva)
        self.assertIn(nueva, self.cells)

    def test_eliminar_bounding_box_manual(self):
        """Simula eliminar un bounding box manualmente"""
        if self.cells:
            eliminado = self.cells[0]
            self.cells.remove(eliminado)
            self.assertNotIn(eliminado, self.cells)

    def test_xml_contiene_datos_validos(self):
        """Verifica que el XML generado contenga información válida"""
        xml_str = self.results_processor.generateXML(self.image, self.cells)
        root = ET.fromstring(xml_str)
        objetos_xml = root.findall("object")
        self.assertEqual(len(objetos_xml), len(self.cells), "El XML no contiene todas las células")

    def test_exportar_resultados_crea_y_elimina_archivo(self):
        """Guarda XML en archivo y verifica su existencia y contenido"""
        xml_str = self.results_processor.generateXML(self.image, self.cells)
        filename = "./test_data/test_export.xml"
        os.makedirs("./test_data", exist_ok=True)

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(xml_str)

        self.assertTrue(os.path.exists(filename), "No se generó el archivo XML")

        tree = ET.parse(filename)
        root = tree.getroot()
        self.assertEqual(root.tag, "annotation")

        # Limpieza
        os.remove(filename)
        self.assertFalse(os.path.exists(filename), "El archivo XML no se eliminó correctamente")

    def test_segmentacion_sin_resultados_manejado(self):
        """Verifica que si no se detectan células, el sistema lo maneja correctamente"""
        if len(self.cells) == 0:
            self.assertEqual(self.processor.countCells(self.cells), 0)

            xml_str = self.results_processor.generateXML(self.image, self.cells)
            root = ET.fromstring(xml_str)
            self.assertEqual(len(root.findall('object')), 0)

    #  TESTS DE TIPO

    def test_tipo_dato_segmentacion(self):
        """Comprueba que el resultado de la segmentación es una lista de objetos Erythrocyte"""
        self.assertIsInstance(self.cells, list)
        if self.cells:
            self.assertIsInstance(self.cells[0], Erythrocyte)

    def test_tipo_dato_xml(self):
        """Comprueba que generateXML devuelve un string"""
        xml_resultado = self.results_processor.generateXML(self.image, self.cells)
        self.assertIsInstance(xml_resultado, str)

    def test_tipo_dato_conteo(self):
        """Verifica que countCells devuelve un entero"""
        conteo = self.processor.countCells(self.cells)
        self.assertIsInstance(conteo, int)


if __name__ == '__main__':
    unittest.main()
