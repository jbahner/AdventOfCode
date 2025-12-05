package jbahner.day04;

import java.util.ArrayList;
import java.util.List;

import jbahner.AbstractDay;
import jbahner.SplitParser;
import jbahner.util.InputReaderException;

public class Day04 extends AbstractDay<List<Day04.PaperRoll>> {

  public Day04() throws InputReaderException {
    super(4, new SplitParser("\n").map(Day04::toPaperRolls));
  }

  static void main() throws Exception {
    run(Day04.class);
  }

  @Override
  public Long part1() {
    return (long) removableRolls(input).size();
  }

  @Override
  public Long part2() {
    long sum = 0;
    List<PaperRoll> rolls;
    do {
      rolls = removableRolls(input);
      sum += rolls.size();
      input.removeAll(rolls);
    } while (!rolls.isEmpty());
    return sum;
  }

  private static List<PaperRoll> removableRolls(List<PaperRoll> rolls) {
    return rolls.stream()
            .filter(pr -> pr.surroundingRolls(rolls) < 4)
            .toList();
  }

  record PaperRoll(int x, int y) {
    long surroundingRolls(List<PaperRoll> rolls) {
      return rolls.stream()
              .filter(pr -> pr != this)
              .filter(pr -> Math.abs(pr.x - x) <= 1)
              .filter(pr -> Math.abs(pr.y - y) <= 1)
              .count();
    }
  }

  private static List<PaperRoll> toPaperRolls(List<String> input) {
    List<PaperRoll> result = new ArrayList<>();
    for (int y = 0; y < input.size(); y++) {
      for (int x = 0; x < input.get(y).length(); x++) {
        if (input.get(y).charAt(x) == '@') {
          result.add(new PaperRoll(x, y));
        }
      }
    }
    return result;
  }
}
