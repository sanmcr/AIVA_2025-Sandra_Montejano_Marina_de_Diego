# Ecosistema del Sistema, Test Automáticos y Mockup

## 1. Ecosistema del Sistema

### 1.1 Descripción General
El sistema de conteo de glóbulos rojos automatizado se integra con un microscopio digital que proporciona imágenes en resolución **VGA (640x480 píxeles)**.  
El software segmenta y cuenta las células presentes en las imágenes capturadas, generando un archivo **XML en formato VOC Pascal** con los datos obtenidos.

### 1.2 Componentes del Sistema
El sistema está compuesto por los siguientes módulos:

- **Microscopio (Fuente de Imágenes):** Captura las imágenes para su procesamiento.
- **Módulo de Captura de Imágenes:** Obtiene imágenes desde la cámara del microscopio y las envía al sistema.
- **Módulo de Procesamiento de Imágenes:** Utiliza OpenCV en Python para segmentar y contar las células.
- **Módulo de Generación de XML:** Convierte los resultados de la segmentación en un archivo **XML en formato VOC Pascal**.
- **Módulo de Visualización:** Muestra la imagen segmentada para la validación manual por parte del técnico.
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
- **Lenguaje de Programación:** Python para el procesamiento de imágenes y generación del XML.
- **Procesamiento de Imágenes:** OpenCV en Python.
- **Framework de Testing:** `unittest` en Python.
- **Generación de XML:** Python con `xml.etree.ElementTree`.
- **Interfaz Gráfica:** Java Swing o JavaFX.

---

## 2. Test Automáticos

### 2.1 Pruebas Unitarias
Se han implementado pruebas unitarias en Python para validar el correcto funcionamiento de los módulos del sistema.  
Las pruebas están enfocadas en:

- **Carga de imágenes:** Verificación de que la imagen se genera correctamente en memoria.
- **Segmentación de células:** Comprobación de que el sistema detecta y segmenta correctamente las células.
- **Generación de XML:** Validación de que el XML generado sigue la estructura correcta en formato **VOC Pascal** y se almacena en `xml_outputs/`.

Ejemplo de pruebas unitarias en Python utilizando `unittest`:

```python
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
```

---

## 3. Mockup del Sistema

El mockup del sistema simula la funcionalidad del conteo de células y la generación de XML para pruebas iniciales.  
Los elementos clave del mockup incluyen:

- **Generación de imágenes simuladas de células.**
- **Segmentación de células utilizando OpenCV.**
- **Generación de un archivo XML con formato VOC Pascal en `xml_outputs/`.**
- **Simulación de errores en la carga y procesamiento de imágenes.**
- **Pruebas automatizadas para verificar que el sistema maneja correctamente imágenes y XML.**

Para generar un archivo XML en el formato correcto, se puede ejecutar el siguiente comando:

```sh
python mockup.py
```

Esto guardará un archivo `resultado.xml` en la carpeta `xml_outputs/`.

---

## 4. Conclusión

Este enfoque basado en test automáticos y mockups permite desarrollar un sistema de conteo de glóbulos rojos confiable, reduciendo errores humanos y optimizando el tiempo de análisis de cada imagen.  
El uso de XML en formato VOC Pascal asegura compatibilidad con estándares de anotación de imágenes para análisis biomédico.
