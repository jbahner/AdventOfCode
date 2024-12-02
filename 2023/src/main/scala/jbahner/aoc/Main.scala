package jbahner.aoc

import scala.io.Source
@main def runAllDays = {
  println(s"Day01, Part01: ${Day01.part1(loadInput("day01"))}")
  println(s"Day01, Part02: ${Day01.part2(loadInput("day01"))}")

  println(s"Day02, Part01: ${Day02.part1(loadInput("day02"))}")
  println(s"Day02, Part02: ${Day02.part2(loadInput("day02"))}")

  // println(s"Day03, Part01: ${Day03.part1(loadInput("day03"))}")
  // println(s"Day03, Part02: ${Day03.part2(loadInput("day02"))}")

  println(s"Day04, Part01: ${Day04.part1(loadInput("day04"))}")
  println(s"Day04, Part02: ${Day04.part2(loadInput("day04-test"))}")
}

def loadInput(day: String): String =
  Source.fromResource(day).getLines().mkString("\n")
