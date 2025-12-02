package jbahner;

import java.util.function.Function;


public interface InputParser<T> {
  T parse(byte[] input);

  default <R> InputParser<R> map(Function<T, R> mapper) {
    return input -> mapper.apply(this.parse(input));
  }
}