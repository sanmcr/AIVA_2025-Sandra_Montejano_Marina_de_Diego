Repositorio para la evolución del trabajo. Sandra Montejano y Marina de Diego.

# AIVA_2025: Conteo de Células de Glóbulos Rojos

## Introducción
Este proyecto tiene como objetivo automatizar el conteo de células de glóbulos rojos en imágenes obtenidas desde un microscopio con cámara integrada. Actualmente, este proceso se realiza manualmente, lo que es tedioso y propenso a errores. Con esta solución, se busca mejorar la eficiencia y reducir costos al permitir que el sistema cuente y segmente las células automáticamente.

## Objetivo
- Implementar un software en **Java** que procese imágenes (640x480) del microscopio.
- Extraer la información de las células y devolver un XML con su distribución.
- Integrar el software con el sistema del microscopio, ejecutándose en su ordenador interno (Windows, Intel i7, 32GB RAM).
- Generar un informe visual en la aplicación de Java con la segmentación de las células.
- Permitir la supervisión de los técnicos de laboratorio para validar los resultados.

## Tecnologías Utilizadas
- **Lenguaje principal:** Java
- **Procesamiento de imágenes (prototipo):** Python + OpenCV
- **Formato de salida:** XML (VOC Pascal)
- **Sistema operativo:** Windows

## Instalación
1. Clonar el repositorio desde GitHub:
   ```sh
   [git clone https://github.com/sanmcr/AIVA_2025-Sandra_Montejano_Marina_de_Diego]
   ```
2. Importar el proyecto en un entorno de desarrollo compatible con Java (Eclipse, IntelliJ IDEA).
3. Instalar dependencias necesarias (OpenCV, XML parsers).
4. Compilar y ejecutar el software.

## Uso
- El software recibirá imágenes desde la aplicación del microscopio.
- Procesará la imagen para detectar y contar células.
- Generará un XML con la distribución de células.
- Presentará la segmentación en pantalla para validación manual.

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

## Documentación del Ecosistema

Puedes encontrar el ecosistema del sistema, las pruebas automáticas y el mockup en el siguiente documento:

📎 [Ver Ecosistema, Tests Automáticos y Mockup](docs/Ecosistema_Tests_Mockup.md)

## Diagrama de Clases UML

El sistema ha sido diseñado de forma modular. Cada clase representa un componente funcional:

- **`CapturaImagen`**: obtiene o carga imágenes.
- **`Imagen`**: representa los datos visuales.
- **`ProcesadorImagenes`**: segmenta y cuenta células.
- **`Celula`**: almacena coordenadas de cada célula detectada.
- **`GeneradorXML`**: exporta resultados en formato XML.
- **`Visualizador`**: muestra resultados en pantalla.
- **`Almacenamiento`**: guarda los resultados generados.

📎 [Ver Diagrama UML](docs/DiagramaClases.png)


