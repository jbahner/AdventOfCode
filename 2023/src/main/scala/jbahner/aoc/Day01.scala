package jbahner.aoc

import scala.collection.mutable.LinkedHashMap
object Day01 extends AoCSolution {
  def parseAndSum(arr: Array[String]) = arr
    .map(line => (line.find(_.isDigit).get, line.findLast(_.isDigit).get))
    .map((c1, c2) => c1.asDigit * 10 + c2.asDigit)
    .fold(0)((x, y) => x + y)

  override def part1(input: String): Int = parseAndSum(input.split("\n"))

  override def part2(input: String): Int = {
    val numbers = LinkedHashMap(
      "oneight" -> "18",
      "twone" -> "21",
      "threeight" -> "38",
      "fiveight" -> "58",
      "sevenine" -> "79",
      "eightwo" -> "82",
      "eighthree" -> "83",
      "nineight" -> "98",
      "one" -> "1",
      "two" -> "2",
      "three" -> "3",
      "four" -> "4",
      "five" -> "5",
      "six" -> "6",
      "seven" -> "7",
      "eight" -> "8",
      "nine" -> "9"
    )
    parseAndSum(
      numbers
        .foldLeft(input)((cur, replacement) =>
          cur.replaceAll(replacement._1, replacement._2)
        )
        .split("\n")
    )
  }
}
