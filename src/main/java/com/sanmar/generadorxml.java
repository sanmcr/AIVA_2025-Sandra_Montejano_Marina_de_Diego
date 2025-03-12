package com.sanmar;

import org.opencv.core.Rect;
import org.w3c.dom.Document;
import org.w3c.dom.Element;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.ParserConfigurationException;
import java.io.File;
import java.util.List;
import javax.xml.transform.*;
import javax.xml.transform.dom.DOMSource;
import javax.xml.transform.stream.StreamResult;

public class GeneradorXML {

    public static void generarXML(List<Rect> celulas, String nombreArchivo) {
        try {
            DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
            DocumentBuilder builder = factory.newDocumentBuilder();
            Document doc = builder.newDocument();

            Element rootElement = doc.createElement("Celulas");
            doc.appendChild(rootElement);

            for (Rect rect : celulas) {
                Element celula = doc.createElement("Celula");
                celula.setAttribute("x", String.valueOf(rect.x));
                celula.setAttribute("y", String.valueOf(rect.y));
                celula.setAttribute("width", String.valueOf(rect.width));
                celula.setAttribute("height", String.valueOf(rect.height));
                rootElement.appendChild(celula);
            }

            TransformerFactory transformerFactory = TransformerFactory.newInstance();
            Transformer transformer = transformerFactory.newTransformer();
            transformer.setOutputProperty(OutputKeys.INDENT, "yes");
            DOMSource source = new DOMSource(doc);
            StreamResult result = new StreamResult(new File(nombreArchivo));
            transformer.transform(source, result);

            System.out.println("Archivo XML generado correctamente.");

        } catch (ParserConfigurationException | TransformerException e) {
            System.err.println("Error al generar XML: " + e.getMessage());
        }
    }
}
