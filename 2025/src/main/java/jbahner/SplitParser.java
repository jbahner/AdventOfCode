package jbahner;

import java.util.Arrays;
import java.util.List;
import java.util.function.Function;

/**
 * Parser for splitting the input string by the given delimiter pattern.
 *
 * @author jba
 */
public class SplitParser implements InputParser<List<String>> {
  private final String delimiter;

  public SplitParser(String delimiter) {
    this.delimiter = delimiter;
  }

  @Override
  public List<String> parse(byte[] input) {
    return new StringParser()
            .map(s -> Arrays.asList(s.split(delimiter)))
            .parse(input);
  }

  public <R> InputParser<List<R>> mapEach(Function<String, R> mapper) {
    return InputParser.super.map(el -> el.stream().map(mapper).toList());
  }
}
