package jbahner.day02;

import java.util.Arrays;
import java.util.List;
import java.util.function.LongPredicate;
import java.util.stream.IntStream;
import java.util.stream.LongStream;

import jbahner.AbstractDay;
import jbahner.SplitParser;
import jbahner.util.InputReaderException;

public class Day02 extends AbstractDay<List<Day02.IdRange>> {

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

    LongStream filter(LongPredicate hasRepeatingPattern) {
      return LongStream.range(lower, upper + 1)
              .filter(hasRepeatingPattern);
    }
  }

  public Day02() throws InputReaderException {
    super(2, new SplitParser(",").mapEach(IdRange::fromInputSlice));
  }

  static void main() throws Exception {
    run(Day02.class);
  }

  private Long solve(LongPredicate hasRepeatingPattern) {
    return input.stream().flatMapToLong(idRange -> idRange.filter(hasRepeatingPattern)).sum();
  }

  @Override
  public Long part1() {
    LongPredicate hasRepeatingPattern = (val) -> {
      String id = String.valueOf(val);
      int middle = id.length() / 2;
      return id.substring(0, middle).equals(id.substring(middle));
    };
    return solve(hasRepeatingPattern);
  }

  @Override
  public Long part2() {
    LongPredicate hasRepeatingPattern = (val) -> {
      String id = String.valueOf(val);
      int idLength = id.length();
      // Only patterns up to half the total length are possible
      for (int i = 1; i <= idLength / 2; i++) {
        String candidate = id.substring(0, i);
        int candidateLength = candidate.length();
        // If the length of the entire ID is not a multiple of the candidate length, we can skip
        if (idLength % candidateLength != 0) continue;
        boolean repeatingPattern = splitIntoChunks(id.substring(candidateLength), candidateLength)
                .stream()
                .allMatch(candidate::equals);
        if (repeatingPattern) return true;
      }
      return false;
    };
    return solve(hasRepeatingPattern);
  }

  private static List<String> splitIntoChunks(String s, int size) {
    return IntStream.iterate(0, i -> i < s.length(), i -> i + size)
            .mapToObj(i -> s.substring(i, Math.min(i + size, s.length())))
            .toList();
  }
}
