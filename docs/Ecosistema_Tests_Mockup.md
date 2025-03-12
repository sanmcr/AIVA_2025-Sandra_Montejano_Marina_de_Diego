# Ecosistema del Sistema, Test Automáticos y Mockup

## 1. Ecosistema del Sistema

### 1.1 Descripción General
El sistema de conteo de glóbulos rojos se integra con un microscopio que proporciona imágenes en resolución VGA (640x480 píxeles). El software procesará estas imágenes para segmentar y contar las células, generando un archivo XML estructurado con la distribución de las células detectadas.

### 1.2 Componentes del Sistema
El sistema está compuesto por los siguientes módulos:

- **Microscopio (Fuente de Imágenes)**: Captura las imágenes para su procesamiento.
- **Módulo de Captura de Imágenes**: Obtiene imágenes desde la cámara del microscopio y las envía al sistema.
- **Módulo de Procesamiento de Imágenes**: Utiliza OpenCV para segmentar y contar las células.
- **Módulo de Generación de XML**: Convierte los resultados de la segmentación en un archivo XML estructurado.
- **Módulo de Visualización**: Muestra la imagen segmentada para la validación manual por parte del técnico.
- **Módulo de Almacenamiento**: Guarda las imágenes procesadas y los archivos XML en el sistema local.
- **Módulo de Exportación**: Permite generar y guardar los archivos XML con los datos procesados.
- **Interfaz de Usuario**: Permite a los técnicos interactuar con el sistema para validar y revisar los resultados.

### 1.3 Flujo del Sistema
El flujo de trabajo del sistema sigue la siguiente estructura:

1. El microscopio captura imágenes y las envía al módulo de captura.
2. El módulo de captura de imágenes procesa la imagen y la envía al módulo de segmentación.
3. El módulo de procesamiento de imágenes (OpenCV) segmenta las células y cuenta la cantidad detectada.
4. Los datos procesados se envían al módulo de generación de XML y a la visualización de resultados.
5. Los técnicos pueden validar los resultados a través de la interfaz de usuario.
6. Si el resultado es válido, se exporta un archivo XML con los datos estructurados.
7. Los datos se almacenan localmente en el sistema para su posterior análisis.

### 1.4 Tecnologías Utilizadas
- **Lenguaje de programación**: Java
- **Procesamiento de imágenes**: OpenCV
- **Framework de testing**: JUnit
- **Automatización de pruebas**: GitHub Actions
- **Generación de XML**: Java DOM Parser
- **Interfaz gráfica**: Java Swing o JavaFX

## 2. Test Automáticos

### 2.1 Pruebas Unitarias
Se implementarán pruebas unitarias para validar el correcto funcionamiento de los módulos del sistema. Las pruebas estarán enfocadas en:

- **Carga de imágenes**: Verificación de que la imagen se carga correctamente en memoria.
- **Segmentación de células**: Comprobación de que el sistema detecta y segmenta correctamente las células.
- **Generación de XML**: Validación de que el XML generado contiene las coordenadas correctas de las células detectadas.

### 2.2 Configuración de GitHub Actions
Se utilizará GitHub Actions para ejecutar los tests automáticamente en cada commit y pull request. El flujo de trabajo incluirá:

1. Clonación del repositorio.
2. Instalación de dependencias.
3. Ejecución de pruebas unitarias con JUnit.
4. Reporte de errores en caso de fallos.

## 3. Mockup del Sistema

Se diseñará un mockup de la interfaz donde se visualizarán los resultados de la segmentación, permitiendo la validación manual del técnico de laboratorio.

El diseño incluirá:

- **Área de visualización de la imagen segmentada**.
- **Indicador del número total de células detectadas**.
- **Botón de validación del conteo**.
- **Opción de exportar los resultados a XML**.

Se utilizará **Figma** o **Balsamiq** para generar un prototipo visual de la interfaz del sistema.

## 4. Conclusión

Este documento presenta el ecosistema del sistema, la planificación de las pruebas automáticas y el diseño del mockup de la interfaz. La implementación de estos elementos garantizará la eficiencia del software, su validación automática y la facilidad de uso para los técnicos de laboratorio.
