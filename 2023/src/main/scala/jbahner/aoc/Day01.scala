package jbahner.aoc

def parseAndSum(arr: Array[String]) = arr
  .map(line => (line.find(_.isDigit).get, line.findLast(_.isDigit).get))
  .map((c1, c2) => c1.asDigit * 10 + c2.asDigit)
  .fold(0)((x, y) => x + y)

def part1(input: String): Int = parseAndSum(input.split("\n"))

def part2(input: String): Int = {
  val numbers = Map(
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
  // TODO: Wrong order of replacements, needs to be from left to right
  parseAndSum(
    input
      .split("\n")
      .map(line => numbers.foldLeft(line)((a, b) => a.replaceAll(b._1, b._2)))
      .map(f => { println(f); f })
  )
}
