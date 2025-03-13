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

- **Carga de imágenes:** Verificación de que la imagen se carga correctamente en memoria desde `JPGImages/`.
- **Segmentación de células:** Comprobación de que el sistema detecta y segmenta correctamente las células.
- **Generación de XML:** Validación de que el XML generado contiene las coordenadas correctas de las células detectadas y se almacena en `annotations/`.

Ejemplo de test unitario en Python utilizando `unittest`:
```python
import unittest
import cv2
import os
from contador_globulos import contar_celulas, generar_xml

class TestContadorGlobulos(unittest.TestCase):
    def test_contar_celulas(self):
        """ Verifica que el contador detecta células en una imagen de prueba. """
        imagen_path = "imagenes_prueba/JPGImages/imagen1.jpg"
        self.assertTrue(os.path.exists(imagen_path), "La imagen de prueba no existe")
        imagen = cv2.imread(imagen_path, 0)  # Imagen en escala de grises
        num_celulas, bboxes = contar_celulas(imagen)
        self.assertGreater(num_celulas, 0, "Debe detectar al menos una célula")
    
    def test_generacion_xml(self):
        """ Verifica que el XML generado es válido. """
        bboxes = [(10, 20, 30, 40), (50, 60, 70, 80)]
        xml_output_path = "imagenes_prueba/annotations/resultado.xml"
        generar_xml(bboxes, xml_output_path)
        self.assertTrue(os.path.exists(xml_output_path), "El XML no se generó correctamente")

if __name__ == '__main__':
    unittest.main()
```

### 2.2 Configuración de GitHub Actions
Se utilizará GitHub Actions para ejecutar los tests automáticamente en cada commit y pull request. El flujo de trabajo incluirá:

1. **Clonación del repositorio.**
2. **Instalación de dependencias.**
3. **Ejecución de pruebas unitarias con `unittest` en Python.**
4. **Reporte de errores en caso de fallos.**

Ejemplo de ejecución en local:
```sh
python -m unittest discover tests
```

---

## 3. Mockup del Sistema

Dado que el sistema debe integrarse con un software en Java, el mockup del sistema consistirá en la implementación de una función que realice la segmentación de células, genere el XML correspondiente y visualice los resultados para su validación manual.

### 3.1 Descripción del Mockup
El mockup implementado en Python servirá como un prototipo que simula el funcionamiento del sistema de detección de células. Este incluirá:

- **Carga de imágenes de prueba desde `JPGImages/`.**
- **Segmentación de células utilizando OpenCV.**
- **Generación de un XML con los resultados de la detección en `annotations/`.**
- **Visualización de las imágenes con bounding boxes.**

Esta implementación permitirá validar la funcionalidad del sistema antes de su integración final con Java.

### 3.2 Validación y Supervisión
Para garantizar que el sistema cumple con los requisitos de los técnicos de laboratorio:
- Se mostrará en pantalla la segmentación de las células antes de confirmar el conteo.
- Se generará un archivo XML con la distribución de las células para que el software del microscopio lo procese.
- Se realizarán pruebas con imágenes reales proporcionadas por el cliente para evaluar la tasa de acierto.

---

## 4. Conclusión
Este enfoque basado en test automáticos y mockups permitirá desarrollar un sistema de conteo de glóbulos rojos confiable, reduciendo errores humanos y optimizando el tiempo de análisis de cada imagen.

