# AIVA_2025 – Conteo de Glóbulos Rojos

Repositorio del sistema de Visión Artificial para el microscopio digital.  
Autoras: Sandra Montejano y Marina de Diego.


## Introducción
Este proyecto tiene como objetivo automatizar el conteo de glóbulos rojos en imágenes obtenidas desde un microscopio con cámara integrada. La solución ha sido empaquetada como una librería `.jar`, diseñada para integrarse en aplicaciones Java.

Internamente, la librería contiene un ejecutable que encapsula el algoritmo de visión artificial desarrollado en Python, por lo que no es necesario instalar Python ni sus dependencias. Esto permite a cualquier desarrollador de software Java integrar fácilmente el sistema en sus aplicaciones sin preocuparse por la configuración del entorno de análisis de imágenes.

## Objetivo
- Desarrollar un sistema de conteo automático de glóbulos rojos a partir de imágenes de microscopio (640x480), utilizando algoritmos de visión artificial en **Python**.
- Extraer la información de las células y devolver un archivo XML con su distribución (formato VOC Pascal).
- Integrar el sistema con el software existente del microscopio, desarrollado en **Java**, ejecutándose en su ordenador interno (Windows, Intel i7, 32GB RAM).
- Generar un informe visual dentro de la aplicación de Java con la segmentación de las células.
- Permitir la supervisión de los técnicos de laboratorio para validar los resultados de forma manual.

> Nota: Toda la lógica del sistema está implementada en el archivo `clases.py`.  
> El script `cellsDetector.py` es el punto de entrada que utiliza estas clases para ejecutar el procesamiento completo.


## Tecnologías Utilizadas
- **Lenguaje principal del algoritmo de visión:** Python
- **Procesamiento de imágenes:** OpenCV
- **Interfaz gráfica y aplicación existente:** Java (microscopio)
- **Formato de comunicación:** XML (VOC Pascal)
- **Sistema operativo objetivo:** Windows (PC integrado en el microscopio)

## Instalación

### Requisitos del sistema

El sistema ha sido diseñado para ser ejecutado con `Python 3.12`. Además, se ha hecho uso de los siguiente paquetes y sus versiones:
- OpenCV 4.10.0
```bash
pip install opencv-python==4.10.0
```
- Numpy 2.2.4
 ```bash
pip install numpy==2.2.4
```
La instalación de las librerías también se puede realizar a través de:
```bash
pip install -r requirements.txt
```

Adicionalmente, el sistema operativo con el que se ha diseñado el sistema es Windows

### Clonar el repositorio
```bash
git clone https://github.com/sanmcr/AIVA_2025-Sandra_Montejano_Marina_de_Diego

cd AIVA_2025-Sandra_Montejano_Marina_de_Diego
```
## Uso del sistema

Una vez instaladas las dependencias, puedes ejecutar el procesamiento de las imágenes con:

```bash
python cellsDetector.py --images_path ./JPEGImages --results_path ./results
```

También puedes añadir el argumento --save_images si deseas guardar las imágenes procesadas con las bounding boxes:

```bash
python cellsDetector.py --images_path ./JPEGImages --results_path ./results --save_images True
```

- `--images_path`: ruta a la carpeta que contiene las imágenes a procesar (obligatorio).
- `--results_path`:  carpeta donde se guardarán los archivos XML generados (obligatorio).
- `--save_images`: si es True, se guardan también las imágenes con las bounding boxes. Por defecto es False, por lo que las imágenes no se guardan a menos que se indique (opcional).


Esto realiza las siguientes tareas:

- Procesa todas las imágenes dentro de la carpeta `./JPEGImages`
- Detecta y cuenta los glóbulos rojos automáticamente
- Genera un archivo XML por imagen con las coordenadas de cada célula en la carpeta `./results`
- Muestra una de las imágenes segmentadas por pantalla para validación visual



 ## Pruebas Automáticas

Este proyecto incluye pruebas unitarias para validar el correcto funcionamiento del sistema de detección y conteo.

### Ejecutar todos los tests:

```bash
python -m unittest unit_test.py
```

### Tests incluidos:

- `test_segmentacion`: verifica que la segmentación devuelve una lista válida de objetos `Erythrocyte`.
- `test_segmentacion_sin_resultados_manejado`: comprueba que el sistema maneja correctamente el caso de no detectar células.
- `test_exportar_resultados_crea_y_elimina_archivo`: crea un archivo XML y luego lo elimina tras comprobar que es correcto.
- `test_carga_imagen_valida`: valida que las imágenes tienen las dimensiones esperadas.
- `test_conteo_celulas`: verifica que el conteo de células coincide con el número de objetos en la lista.
- `test_agregar_bounding_box_manual` y `test_eliminar_bounding_box_manual`: simulan edición manual de regiones detectadas.
- `test_tipo_dato_segmentacion`: valida que el resultado de la segmentación es una lista de `Erythrocyte`.
- `test_tipo_dato_xml`: valida que el XML generado es un `str`.
- `test_tipo_dato_conteo`: verifica que el conteo de células devuelve un `int`.


## Integración con Java

El algoritmo de conteo de células ha sido desarrollado en Python por su facilidad para el procesamiento de imágenes. El microscopio ya cuenta con un software en Java que proporcionará las imágenes. El flujo de integración es el siguiente:

1. El software Java guarda la imagen capturada.
2. Se ejecuta el script de Python, que procesa la imagen y genera un archivo `XML`.
3. El software Java interpreta el `XML` y muestra los resultados al técnico de laboratorio.

Este enfoque permite mantener la interfaz actual y facilitar la integración dentro del sistema ya desplegado.

## Contribución
1. Crear una nueva rama para cada nueva funcionalidad o corrección de errores.
2. Relacionar cada commit con su respectiva issue.
3. Enviar un pull request con una descripción clara de los cambios.

## Licencia

Este software está protegido por derechos de autor (copyright) y no es de código abierto.  
Todos los derechos están reservados a  VisioTech AI.  

Queda estrictamente prohibida la reproducción, distribución o modificación del software sin el consentimiento expreso y por escrito de los titulares de los derechos.  

### Derechos de Uso
- El software solo puede ser utilizado por las entidades y personas autorizadas.  
- No se permite la copia, redistribución ni la ingeniería inversa del código.  
- La documentación adjunta también está protegida por copyright.  

### Nota Legal
El uso no autorizado de este software puede dar lugar a sanciones legales conforme a las leyes de propiedad intelectual vigentes.  


## Contacto
Para más información, contactar con el equipo de desarrollo a través de GitHub Issues.




