package com.sanmar;

import org.junit.jupiter.api.Test;
import org.opencv.core.Rect;

import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

class ProcesadorImagenesTest {

    @Test
    void testSegmentacionCelulas() {
        List<Rect> celulas = ProcesadorImagenes.segmentarCelulas("src/test/resources/sample_image.jpg");

        assertNotNull(celulas, "La lista de células no debería ser nula.");
        assertTrue(celulas.size() >= 0, "El número de células detectadas debe ser mayor o igual a 0.");
    }
}
