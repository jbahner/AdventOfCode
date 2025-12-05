package jbahner;

import java.time.Duration;
import java.time.Instant;
import java.util.function.Supplier;

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
    ExecutionResult part1 = executeMeasured(day::part1);
    System.out.println("Part 1: " + part1.result() + " (" + part1.executionTime().toMillis() + " ms)");

    ExecutionResult part2 = executeMeasured(day::part2);
    System.out.println("Part 2: " + part2.result() + " (" + part2.executionTime().toMillis() + " ms)");
  }

  record ExecutionResult(long result, Duration executionTime) {
  }

  private static ExecutionResult executeMeasured(Supplier<Long> r) {
    Instant start = Instant.now();
    long result = r.get();
    Instant end = Instant.now();
    Duration duration = Duration.between(start, end);
    return new ExecutionResult(result, duration);
  }
}
