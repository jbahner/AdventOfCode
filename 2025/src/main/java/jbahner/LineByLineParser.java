package jbahner;

import java.nio.charset.StandardCharsets;
import java.util.List;

public class LineByLineParser implements InputParser<List<String>> {

  @Override
  public List<String> parse(byte[] input) {
    return new String(input, StandardCharsets.UTF_8).lines().toList();

  }
}
