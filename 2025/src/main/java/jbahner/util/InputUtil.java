package jbahner.util;

import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Optional;
import java.util.logging.Logger;

import io.github.cdimascio.dotenv.Dotenv;

public class InputUtil {

  private static final Logger LOG = Logger.getLogger(InputUtil.class.getName());
  private static final String FILE_FORMAT = "day%02d.txt";

  /**
   * Reads the input of the given day. Inputs are expected as <code>day<#daynum>.txt</code>, where #daynum is formatted to 2 digits (day 2 -> day02.txt).
   * Since the test resources are earlier in the runtime classpath, the test input is always taken if run in test mode.
   *
   * @param day The day to read the input for
   * @return The content of the input file
   * @throws IOException If the input file is missing or an error occurred while reading
   */
  public static byte[] readInput(int day) throws InputReaderException {
    String fileName = String.format(FILE_FORMAT, day);
    try {
      if (Thread.currentThread().getContextClassLoader().getResource(fileName) == null) {
        LOG.info("Input file not found locally, attempting to download...");
        return downloadInput(day);
      }
      downloadInput(day);
      try (InputStream in = Thread.currentThread()
              .getContextClassLoader()
              .getResourceAsStream(fileName);
           ByteArrayOutputStream out = new ByteArrayOutputStream()) {

        if (in == null) {
          throw new IllegalArgumentException("Resource not found: " + fileName);
        }

        in.transferTo(out);
        return out.toByteArray();
      }
    } catch (Exception e) {
      throw new InputReaderException(e.getMessage(), e);
    }
  }

  private static byte[] downloadInput(int day) throws IOException, InterruptedException {
    String fileName = String.format(FILE_FORMAT, day);
    Dotenv env = Dotenv.load();
    String token = Optional.ofNullable(env.get("AOC_TOKEN")).orElseThrow();

    String url = "https://adventofcode.com/2025/day/" + day + "/input";
    try (HttpClient client = HttpClient.newHttpClient()) {
      HttpRequest request = HttpRequest.newBuilder()
              .uri(URI.create(url))
              .header("Cookie", "session=" + token)
              .build();

      HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
      if (response.statusCode() != 200) {
        throw new RuntimeException("Failed to retrieve input. HTTP code : " + response.statusCode());
      }
      Path inputFile = Path.of("src/main/resources").resolve(fileName);
      String body = response.body();
      Files.writeString(inputFile, body);
      LOG.info("Successfully downloaded input file: " + inputFile);
      return body.getBytes(StandardCharsets.UTF_8);
    }
  }

}
