package jbahner.day03;

import java.util.List;

import jbahner.AbstractDay;
import jbahner.SplitParser;
import jbahner.util.InputReaderException;

public class Day03 extends AbstractDay<List<String>> {

  public Day03() throws InputReaderException {
    super(3, new SplitParser("\n"));
  }

  static void main() throws Exception {
    run(Day03.class);
  }

  @Override
  public Long part1() {
    long sum = 0;
    for (String line : input) {
      List<Integer> digits = line.chars().map(Character::getNumericValue).boxed().toList();
      String result = findHighestDigits(digits, 2);
      sum += Long.parseLong(result);
    }
    return sum;
  }

  @Override
  public Long part2() {
    long sum = 0;
    for (String line : input) {
      List<Integer> digits = line.chars().map(Character::getNumericValue).boxed().toList();
      String result = findHighestDigits(digits, 12);
      sum += Long.parseLong(result);
    }
    return sum;
  }

  /**
   * Recursive function that finds the highest digits from in order from left to right with the given
   * length and returns them concatenated as a string.
   *
   * @param digits The digits to choose from
   * @param length The length of the output string
   * @return The highest possible digits in order
   */
  private String findHighestDigits(List<Integer> digits, int length) {
    if (length == 0) return "";
    // We can only search in the part that leaves enough trailing digits to choose from
    int bound = digits.size() - length;
    int highestDigitIdx = 0;
    for (int i = 1; i <= bound; i++) {
      if (digits.get(i) > digits.get(highestDigitIdx)) highestDigitIdx = i;
    }
    // Take the found digit and search for highest digits in the remaining list of digits
    return digits.get(highestDigitIdx).toString() + findHighestDigits(digits.subList(highestDigitIdx + 1, digits.size()), length - 1);
  }
}
