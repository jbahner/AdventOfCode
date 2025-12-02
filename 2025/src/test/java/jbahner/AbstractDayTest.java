package jbahner;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

public abstract class AbstractDayTest<D extends AbstractDay<?>> {

  private final Class<D> clazz;
  private final Long expectedPart1;
  private final Long expectedPart2;

  protected AbstractDayTest(Class<D> clazz, Long expectedPart1, Long expectedPart2) {
    this.clazz = clazz;
    this.expectedPart1 = expectedPart1;
    this.expectedPart2 = expectedPart2;
  }

  private D createDay() throws Exception {
    return clazz.getDeclaredConstructor().newInstance();
  }


  @Test
  void part1() throws Exception {
    D day = createDay();
    assertEquals(expectedPart1, day.part1());
  }

  @Test
  void part2() throws Exception {
    D day = createDay();
    assertEquals(expectedPart2, day.part2());
  }

}
