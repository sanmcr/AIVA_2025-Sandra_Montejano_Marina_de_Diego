package grupocelulas.detector;

import java.io.*;
import java.nio.file.Files;
import java.nio.file.StandardCopyOption;
import java.util.ArrayList;
import java.util.List;

public class DetectorEritrocitos {

    private final File exeTemporal;

    public DetectorEritrocitos() throws IOException {
        this.exeTemporal = extraerExeTemporario();
    }

    private File extraerExeTemporario() throws IOException {
        InputStream exeStream = getClass().getResourceAsStream("/cellsDetector.exe");
        if (exeStream == null) {
            throw new FileNotFoundException("No se encontró 'cellsDetector.exe' como recurso.");
        }

        File exeTemp = File.createTempFile("cellsDetector", ".exe");
        exeTemp.deleteOnExit(); // Se borra al cerrar el programa

        Files.copy(exeStream, exeTemp.toPath(), StandardCopyOption.REPLACE_EXISTING);
        return exeTemp;
    }

    public List<String> detectar(String carpetaImagenes, String carpetaResultados, boolean guardarImagenes) throws IOException {
        List<String> resultados = new ArrayList<>();

        ProcessBuilder pb = new ProcessBuilder(
                exeTemporal.getAbsolutePath(),
                "--images_path", carpetaImagenes,
                "--results_path", carpetaResultados,
                "--save_images", String.valueOf(guardarImagenes)
        );

        pb.redirectErrorStream(true);
        Process process = pb.start();

        try (BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()))) {
            String linea;
            while ((linea = reader.readLine()) != null) {
                resultados.add(linea);
            }
        }

        return resultados;
    }
}