# Ecosistema del Sistema, Test Automáticos y Mockup

## 1. Ecosistema del Sistema

### 1.1 Descripción General
El sistema de conteo de glóbulos rojos automatizado se integra con un microscopio digital que proporciona imágenes en resolución **VGA (640x480 píxeles)**. El software segmenta y cuenta las células presentes en las imágenes capturadas, generando un archivo **XML estructurado** con los datos obtenidos.

### 1.2 Componentes del Sistema
El sistema está compuesto por los siguientes módulos:

- **Microscopio (Fuente de Imágenes):** Captura las imágenes para su procesamiento.
- **Módulo de Captura de Imágenes:** Obtiene imágenes desde la cámara del microscopio y las envía al sistema.
- **Módulo de Procesamiento de Imágenes:** Utiliza OpenCV en Python para segmentar y contar las células.
- **Módulo de Generación de XML:** Convierte los resultados de la segmentación en un archivo XML estructurado.
- **Módulo de Visualización:** Muestra la imagen segmentada con bounding boxes para la validación manual por parte del técnico.
- **Módulo de Almacenamiento:** Guarda las imágenes procesadas y los archivos XML en el sistema local.
- **Módulo de Exportación:** Permite generar y guardar los archivos XML con los datos procesados.
- **Interfaz de Usuario:** Permite a los técnicos interactuar con el sistema para validar y revisar los resultados.

### 1.3 Flujo del Sistema
El flujo de trabajo del sistema sigue la siguiente estructura:

1. El microscopio captura imágenes y las envía al módulo de captura.
2. El módulo de captura de imágenes procesa la imagen y la envía al módulo de segmentación.
3. El módulo de procesamiento de imágenes (Python + OpenCV) segmenta las células y cuenta la cantidad detectada.
4. Los datos procesados se envían al módulo de generación de XML y a la visualización de resultados.
5. Los técnicos pueden validar los resultados a través de la interfaz de usuario.
6. Si el resultado es válido, se exporta un archivo XML con los datos estructurados.
7. Los datos se almacenan localmente en el sistema para su posterior análisis.

### 1.4 Tecnologías Utilizadas
- **Lenguaje de Programación:** Python para el procesamiento de imágenes y generación del XML, Java para la integración con la aplicación del microscopio.
- **Procesamiento de Imágenes:** OpenCV en Python.
- **Framework de Testing:** `unittest` en Python.
- **Automatización de Pruebas:** GitHub Actions.
- **Generación de XML:** Python con `xml.etree.ElementTree`.
- **Interfaz Gráfica:** Java Swing o JavaFX.

---

## 2. Test Automáticos

### 2.1 Pruebas Unitarias
Se implementarán pruebas unitarias en Python para validar el correcto funcionamiento de los módulos del sistema. Las pruebas estarán enfocadas en:

- **Carga de imágenes:** Verificación de que la imagen se carga correctamente en memoria desde `img/JPGImages/`.
- **Segmentación de células:** Comprobación de que el sistema detecta y segmenta correctamente las células.
- **Generación de XML:** Validación de que el XML generado contiene las coordenadas correctas de las células detectadas y se almacena en `img/annotations/`.
- **Visualización:** Comprobación de que la imagen segmentada se muestra correctamente con los bounding boxes.

Ejemplo de pruebas unitarias en Python utilizando `unittest`:

```python
import unittest
import cv2
import os
import xml.etree.ElementTree as ET
from src.python.mockup import contar_celulas, generar_xml, mostrar_bounding_boxes

class TestContadorGlobulos(unittest.TestCase):

    def setUp(self):
        """ Configuración inicial: Define rutas de prueba. """
        self.imagen_path = "img/JPGImages/imagen1.jpg"
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

    def test_generacion_xml(self):
        """ Verifica que el XML generado contiene la estructura correcta. """
        bboxes = [(10, 20, 30, 40), (50, 60, 70, 80)]
        generar_xml(bboxes, self.xml_output_path)

        self.assertTrue(os.path.exists(self.xml_output_path), "El XML no se generó correctamente.")
        tree = ET.parse(self.xml_output_path)
        root = tree.getroot()
        self.assertEqual(root.tag, "celulas", "El XML debe contener una etiqueta <celulas>.")
        os.remove(self.xml_output_path)

if __name__ == '__main__':
    unittest.main()
```

---

## 3. Mockup del Sistema

El mockup del sistema simula la funcionalidad del conteo de células y la generación de XML para pruebas iniciales.

- **Carga de imágenes desde `img/JPGImages/`.**
- **Segmentación de células utilizando OpenCV.**
- **Generación de un XML en `img/annotations/`.**
- **Visualización de imágenes segmentadas con bounding boxes.**

---

## 4. Conclusión
Este enfoque basado en test automáticos y mockups permitirá desarrollar un sistema de conteo de glóbulos rojos confiable, reduciendo errores humanos y optimizando el tiempo de análisis de cada imagen.

