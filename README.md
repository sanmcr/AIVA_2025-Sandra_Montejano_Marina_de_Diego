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

> Nota: La lógica interna del sistema fue desarrollada en Python, pero ha sido encapsulada en un ejecutable que está integrado en la librería `.jar`, por lo que el usuario no necesita acceder ni ejecutar ningún script directamente.



## Tecnologías Utilizadas
- **Lenguaje principal del algoritmo de visión:** Python
- **Procesamiento de imágenes:** OpenCV
- **Interfaz gráfica y aplicación existente:** Java (microscopio)
- **Formato de comunicación:** XML (VOC Pascal)
- **Sistema operativo objetivo:** Windows (PC integrado en el microscopio)

## Uso de la librería `.jar`

Esta herramienta se distribuye como una librería Java en formato `.jar` que se puede integrar fácilmente en cualquier proyecto Java.

### Requisitos
- Java 8 o superior
- Java Development Kit (JDK)
- IDE recomendado: IntelliJ IDEA, Eclipse, NetBeans, etc.

### Instrucciones de integración

1. Descarga el archivo desde la sección [Releases de GitHub](https://github.com/sanmcr/AIVA_2025-Sandra_Montejano_Marina_de_Diego/releases).
2. Copia el archivo `detector-eritrocitos-1.0.0.jar` en una carpeta dentro de tu proyecto (por ejemplo, `lib/`).
3. Añádelo al classpath de tu proyecto:
   - IntelliJ: clic derecho en el `.jar` → `Add as Library`.
   - Eclipse: clic derecho en el proyecto → `Build Path` → `Add External JARs`.
4. Importa la clase principal en tu código:
```java
import grupocelulas.detector.DetectorEritrocitos;
```
5. Llama a la función detectar:
```java
DetectorEritrocitos detector = new DetectorEritrocitos();

List<String> resultados = detector.detectar(
    "C:\\ruta\\a\\imagenes", 
    "C:\\ruta\\a\\resultados", 
    true);
```

> Nota:  recuerda usar rutas absolutas o correctamente formateadas para tu sistema operativo (por ejemplo, con doble barra invertida en Windows).

Esto generará archivos XML con las coordenadas de las células detectadas.

## Integración con Java

El sistema se ha empaquetado como una librería `.jar` que puede integrarse en cualquier proyecto Java.

La clase principal `DetectorEritrocitos` permite realizar el análisis automático de imágenes mediante la función `detectar`, que recibe como parámetros:

- La ruta a la carpeta con las imágenes.
- La ruta de salida para los archivos XML generados.
- Una bandera `true/false` para indicar si se desea guardar las imágenes procesadas.

El archivo `.jar` incluye internamente un ejecutable que encapsula la lógica del procesamiento, por lo que no es necesario instalar Python ni bibliotecas externas. Todo el procesamiento se realiza de forma transparente para el usuario Java.

## Pruebas internas del sistema

Antes de empaquetar el sistema como una librería `.jar`, se desarrollaron pruebas unitarias sobre el núcleo del algoritmo de visión artificial implementado en Python.

Estas pruebas permitieron validar la segmentación de glóbulos rojos, la generación de XML y el comportamiento ante imágenes con y sin células detectables.

> Nota: estas pruebas están dirigidas a desarrolladores. No es necesario ejecutarlas para utilizar la librería Java.

### Ejecutar las pruebas

Si deseas revisar o extender el comportamiento interno, puedes ejecutar los tests con:

```bash
python -m unittest unit_test.py
```

Archivo relacionado: `unit_test.py`, ubicado en el directorio raíz del repositorio.


## Contribución

Este apartado se ha utilizado para gestionar las tareas del proyecto, incluyendo estimaciones de tiempo e issues no previstas.

- Todas las funcionalidades implementadas están registradas como *issues* y han sido marcadas como cerradas una vez completadas.
- Se ha indicado el tiempo estimado inicialmente y el tiempo real empleado en cada tarea.
- En caso de que surgieran modificaciones o funcionalidades no contempladas al inicio, se han añadido nuevas issues para reflejarlo.

Además, durante el desarrollo:
1. Se ha trabajado con ramas separadas para nuevas funcionalidades y correcciones.
2. Cada commit se ha vinculado a su issue correspondiente.
3. Se han seguido buenas prácticas de control de versiones con pull requests claros y documentados.

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




