package jbahner;

import java.nio.charset.StandardCharsets;

/**
 * Converts the byte array to a {@link String}. Probably the base parser for all days.
 *
 * @author jba
 */
public class StringParser implements InputParser<String> {
  @Override
  public String parse(byte[] input) {
    return new String(input, StandardCharsets.UTF_8);
  }
}
