package jbahner.day01;

import java.io.IOException;
import java.time.temporal.ValueRange;
import java.util.List;

import jbahner.AbstractDay;
import jbahner.LineByLineParser;
import jbahner.util.InputReaderException;

/**
 * @see <a href=https://adventofcode.com/2025/day/1>Puzzle</a>
 * @author jba
 */
public class Day01 extends AbstractDay<List<Integer>> {
  private static final int STARTING_POSITION = 50;

  public Day01() throws InputReaderException {
    super(1, new LineByLineParser().map(Day01::toIntRotations));
  }

  private static List<Integer> toIntRotations(List<String> lines) {
    return lines.stream()
            .map(s -> s.replace("L", "-").replace("R", ""))
            .map(Integer::parseInt)
            .toList();
  }

  static void main() throws Exception {
    run(Day01.class);
  }

  @Override
  public Object part1() {
    int cur = STARTING_POSITION;
    int result = 0;
    for (int rotation : input) {
      cur = Math.floorMod(cur + rotation, 100);
      if (cur == 0) result++;
    }
    return result;
  }

  @Override
  public Object part2() {
    ValueRange valueRange = ValueRange.of(1, 99);
    int cur = STARTING_POSITION;
    int result = 0;
    for (int rotation : input) {
      int notNormalizedPosition = cur + (rotation % 100);
      if(cur != 0 && !valueRange.isValidIntValue(notNormalizedPosition)) result++;
      cur = Math.floorMod(cur + rotation, 100);
      int fullRotations = Math.abs(rotation) / 100;
      result += fullRotations;
    }
    return result;
  }
}
