package jbahner.util;

public class InputReaderException extends Exception {

  public InputReaderException(String message, Throwable cause) {
    super(message, cause);
  }

  public InputReaderException(String message) {
    super(message);
  }

  public InputReaderException(Throwable cause) {
    super(cause);
  }
}
