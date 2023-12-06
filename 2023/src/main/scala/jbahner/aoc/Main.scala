package jbahner.aoc

import scala.io.Source
@main def runAllDays = {
  println(s"Day01, Part01: ${part1(loadInput("day01"))}")
  println(s"Day01, Part02: ${part2(loadInput("day01"))}")
}

def loadInput(day: String): String =
  Source.fromResource(day).getLines().mkString("\n")
