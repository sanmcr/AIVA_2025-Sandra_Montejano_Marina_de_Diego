#  Tests del Sistema de Conteo de Glóbulos Rojos

Este módulo contiene las pruebas automáticas desarrolladas para validar el funcionamiento del sistema final de detección y conteo de eritrocitos en imágenes de microscopio.

---

##  Archivos

- `unit_test.py`: contiene los tests principales del sistema real implementado en `clases.py`.

---

##  Cómo ejecutar los tests

Desde la carpeta raíz del proyecto, ejecuta el siguiente comando:

```bash
python -m unittest tests/unit_test.py
```


## Qué se comprueba

El archivo incluye pruebas que validan:

- Carga y validación de una imagen.
- Segmentación de eritrocitos (tipo, estructura, presencia).
- Conteo de células y consistencia con la lista de resultados.
- Edición manual de bounding boxes.
- Generación y validez del archivo XML (formato VOC Pascal).
- Tipos de retorno correctos de las funciones clave.

## Dependencias

Instala los requisitos necesarios con:

```bash
pip install -r requirements.txt
```
