package jbahner;

import java.nio.charset.StandardCharsets;

public class StringParser implements InputParser<String> {
  @Override
  public String parse(byte[] input) {
    return new String(input, StandardCharsets.UTF_8);
  }
}
