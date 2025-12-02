package jbahner.day02;

import java.util.Arrays;
import java.util.List;
import java.util.stream.LongStream;

import jbahner.AbstractDay;
import jbahner.SplitParser;
import jbahner.util.InputReaderException;

public class Day02 extends AbstractDay<List<Day02.IdRange>> {

  public Day02() throws InputReaderException {
    super(2, new SplitParser(",").mapEach(IdRange::fromInputSlice));
  }

  static void main() throws Exception {
    run(Day02.class);
  }

  @Override
  public Long part1() {
    return input.stream().flatMapToLong(IdRange::filterInvalids).sum();
  }

  // Here I assume that all given inputs are actual IDs, so no leading 0 is present
  record IdRange(long lower, long upper) {
    static IdRange fromInputSlice(String slice) {
      List<Long> parts = Arrays.stream(slice.split("-"))
              .map(String::trim)
              .map(Long::parseLong)
              .toList();
      assert parts.size() == 2;
      return new IdRange(parts.getFirst(), parts.getLast());
    }

    LongStream filterInvalids() {
      return LongStream.range(lower, upper + 1)
              .filter(IdRange::isValid);
    }

    static boolean isValid(long id) {
      String str = String.valueOf(id);
      return str.substring(0, str.length() / 2).equals(str.substring(str.length() / 2));
    }
  }

  @Override
  public Long part2() {
    return null;
  }
}
