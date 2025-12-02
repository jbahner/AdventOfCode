package jbahner;

import jbahner.util.InputReaderException;
import jbahner.util.InputUtil;

public abstract class AbstractDay<T> {

  protected T input;

  protected AbstractDay(int day, InputParser<T> parser) throws InputReaderException {
    this.input = parser.parse(InputUtil.readInput(day));
  }

  public abstract Long part1();

  public abstract Long part2();

  public static <D extends AbstractDay<?>> void run(Class<D> clazz) throws Exception {
    D day = clazz.getDeclaredConstructor().newInstance();
    System.out.println("Part 1: " + day.part1());
    System.out.println("Part 2: " + day.part2());
  }
}
