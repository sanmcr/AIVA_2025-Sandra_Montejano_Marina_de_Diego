import grupocelulas.detector.DetectorEritrocitos;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        try {
            // Crear una instancia del detector
            DetectorEritrocitos detector = new DetectorEritrocitos();

            // Ejecutar la detección y obtener los resultados
            List<String> resultados = detector.detectar("C:\\Users\\marin\\PycharmProjects\\ProyectoAICVA\\JPEGImages", "C:\\Users\\marin\\PycharmProjects\\ProyectoAICVA\\results", false);

            // Imprimir los resultados
            for (String resultado : resultados) {
                System.out.println("Resultado: " + resultado);
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
