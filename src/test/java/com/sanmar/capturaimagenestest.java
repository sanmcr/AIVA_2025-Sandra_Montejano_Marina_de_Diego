package com.sanmar;

import org.junit.jupiter.api.Test;
import java.awt.image.BufferedImage;

import static org.junit.jupiter.api.Assertions.*;

class CapturaImagenesTest {

    @Test
    void testCargarImagen() {
        BufferedImage imagen = CapturaImagenes.cargarImagen("src/test/resources/sample_image.jpg");

        assertNotNull(imagen, "La imagen cargada no debería ser nula.");
    }
}
