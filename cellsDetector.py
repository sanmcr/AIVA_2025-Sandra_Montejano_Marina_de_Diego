from clases import AppCore, ImageManager, ImageProcessor, ResultsProcessor, JavaIntegrator
import os
import argparse

# Argumentos de línea de comandos
parser = argparse.ArgumentParser(description="Procesamiento de imágenes para detección de eritrocitos.")
parser.add_argument('--images_path', type=str, help='Ruta al directorio de imágenes')
parser.add_argument('--results_path', type=str, help='Ruta al directorio de resultados')
parser.add_argument('--save_images', type=bool, help='Guardar imágenes procesadas con las detecciones')
args = parser.parse_args()

# Rutas
images_path = args.images_path
results_path = args.results_path
save_images = args.save_images

if not os.path.exists(results_path):
    os.makedirs(results_path)

# Inicialización
app_core = AppCore()
image_processor = ImageProcessor()
results_processor = ResultsProcessor()
java_integrator = JavaIntegrator()

# Simular recepción de órdenes desde Java
java_integrator.receiveRequest(["Procesar imágenes desde JPEGImages/"])

# Obtener imágenes
images_list = os.listdir(images_path)
images_list = app_core.getImagePaths(images_list)

# Procesar cada imagen
for image_path in images_list:
    image_manager = ImageManager(os.path.join(images_path, image_path))
    this_image = image_manager.readImage()
    valid = image_manager.validateImage(this_image)

    if valid:
        image_cells_list = image_processor.processImage(this_image)
        num_cells = image_processor.countCells(image_cells_list)
        print(f'El número de eritrocitos encontrados es: {num_cells} eritrocitos')

        xml_result = results_processor.generateXML(this_image, image_cells_list)
        app_core.saveResults(results_path, xml_result, this_image)

        if save_images:
            app_core.saveImage(results_path, this_image, image_cells_list)

        # Enviar resultados a Java
        java_integrator.sendResults([
            f"{this_image.path}: {num_cells} eritrocitos detectados"
        ])
