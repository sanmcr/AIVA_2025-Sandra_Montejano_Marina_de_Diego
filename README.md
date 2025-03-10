# AIVA_2025-Sandra_Montejano_Marina_de_Diego
Repositorio para la evolución del trabajo 

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
- **Procesamiento de imágenes:** OpenCV (Java)
- **Formato de salida:** XML
- **Sistema operativo:** Windows

## Instalación
1. Clonar el repositorio desde GitHub:
   ```sh
   git clone https://github.com/tuusuario/AIVA_2024_ConteoCelulas.git
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
Definir si el software se venderá bajo licencia o será de código abierto.

## Contacto
Para más información, contactar con el equipo de desarrollo a través de GitHub Issues.
