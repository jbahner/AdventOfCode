package jbahner.aoc

import scala.io.Source
@main def runAllDays = {
  val test = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""
  println(s"Day01, Part01: ${part1(loadInput("day01"))}")
  println(s"Day01, Part02: ${part2(test)}")
}

def loadInput(day: String): String =
  Source.fromResource(day).getLines().mkString("\n")
