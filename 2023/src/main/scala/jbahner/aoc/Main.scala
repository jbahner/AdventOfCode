package jbahner.aoc

import scala.io.Source
@main def runAllDays = {
  println(s"Day01, Part01: ${Day01.part1(loadInput("day01"))}")
  println(s"Day01, Part02: ${Day01.part2(loadInput("day01"))}")

  println(s"Day02, Part01: ${Day02.part1(loadInput("day02"))}")
  println(s"Day02, Part02: ${Day02.part2(loadInput("day02"))}")
}

def loadInput(day: String): String =
  Source.fromResource(day).getLines().mkString("\n")
