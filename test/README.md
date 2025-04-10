# TTests del Sistema de Conteo de Glóbulos Rojos

Este módulo contiene las pruebas automáticas desarrolladas para validar el funcionamiento del sistema final de detección y conteo de eritrocitos en imágenes de microscopio.

---

##  Archivos

- `unit_test.py`: contiene los tests principales del sistema real implementado en `clases.py`.

---

## Cómo ejecutar los tests

Desde la carpeta raíz del proyecto, ejecuta el siguiente comando:

```bash
python -m unittest tests/unit_test.py


1. Abrir una terminal o línea de comandos en la carpeta del proyecto.
2. Ejecutar el siguiente comando:

```bash
python -m unittest test_conteo_celulas.py
```

Si los tests se ejecutan correctamente, se mostrará un resultado similar al siguiente:

```
.....
----------------------------------------------------------------------
Ran 4 tests in 0.004s

OK
```

---

## 4. Cómo Generar y Ver el XML

Para generar un archivo XML con células detectadas, ejecutar el siguiente comando:

```bash
python mockup.py
```

Esto creará un archivo XML en la carpeta `xml_outputs/` con el formato VOC Pascal.  
Para visualizar el XML generado, puedes abrirlo con un editor de texto o en un navegador web.  
Por defecto, el archivo se llama `resultado.xml`.

---

## 5. Explicación de los Tests

Cada test verifica una funcionalidad específica del mockup:

- **test_mockup_generacion**: Verifica que la imagen generada tenga el tamaño y formato correctos.
- **test_mockup_conteo**: Verifica que el mockup cuenta correctamente las células detectadas.
- **test_mockup_conteo_imagen_invalida**: Comprueba que se maneja correctamente una imagen inválida.
- **test_mockup_exportar_xml**: Verifica que el XML generado tiene la estructura correcta con la etiqueta `<annotation>`.

---

## 6. Errores Comunes y Soluciones

**Error:** `ModuleNotFoundError: No module named 'mockup'`  
**Solución:** Asegurarse de que el archivo `mockup.py` esté en la misma carpeta que `test_conteo_celulas.py`.

**Error:** `ImportError: cannot import name 'mockup'`  
**Solución:** Ejecutar los tests desde la carpeta correcta utilizando:

```bash
cd /ruta/del/proyecto
python -m unittest test_conteo_celulas.py
```

**Error:** `AssertionError: 'annotation' != 'Resultados'`  
**Solución:** El XML ahora usa el formato VOC Pascal, la raíz del XML debe ser `<annotation>`, asegúrate de que el test está actualizado.

---

## 7. Autor

Sandra Montejano Cánovas y Marina de Diego Peña  
Proyecto desarrollado para la asignatura Aplicaciones industriales y comerciales.

---

Este documento proporciona las instrucciones necesarias para la ejecución de los tests y la validación del mockup antes de implementar el código real.

