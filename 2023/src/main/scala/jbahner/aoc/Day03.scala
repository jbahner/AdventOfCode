package jbahner.aoc

import scala.util.control.Breaks.*
object Day03 extends AoCSolution {

  val EMPTY_CHAR = '.'

  case class Number(line: Int, start: Int, length: Int, value: Int) {
    def isValid(matrix: Array[Array[Char]]): Boolean = {
      // Check above and below
      // val lol = for {
      //   lineIdx <- List(line - 1, line + 1)
      //   charIdx <- (start - 1) to (start + length + 1)
      //   if (lineIdx >= 0 && lineIdx < matrix.length && charIdx >= 0 && charIdx < matrix(
      //     lineIdx
      //   ).length && matrix(lineIdx)(charIdx) != EMPTY_CHAR)
      // } yield true
      var hasNeighbor = false
      breakable {
        for (lineIdx <- List(line - 1, line + 1)) {
          for (charIdx <- (start - 1) to (start + length + 1)) {
            if (
              lineIdx >= 0 && lineIdx < matrix.length && charIdx >= 0 && charIdx < matrix(
                lineIdx
              ).length && matrix(lineIdx)(charIdx) != EMPTY_CHAR && !matrix(
                lineIdx
              )(charIdx).isDigit
            ) {
              hasNeighbor = true
              break()
            }
          }
        }
        for (charIdx <- List(start - 1, start + length)) {
          if (
            line >= 0 && line < matrix.length && charIdx >= 0 && charIdx < matrix(
              line
            ).length && matrix(line)(charIdx) != EMPTY_CHAR && !matrix(line)(
              charIdx
            ).isDigit
          ) {
            hasNeighbor = true
            break()
          }
        }
      }

      hasNeighbor
    }
  }

  override def part1(input: String): Int = {
    val EMPTY_CHAR = '.'
    val lines = input.split("\n")
    val matrix = Array.ofDim[Char](lines.size, lines(0).length())
    var numbers = List[Number]()
    for (lineIdx <- 0 until lines.size) {
      var start = -1
      for (charIdx <- 0 until lines(lineIdx).length) {
        matrix(lineIdx)(charIdx) = lines(lineIdx)(charIdx)

        if (lines(lineIdx)(charIdx).isDigit) {
          if (start == -1) start = charIdx
        } else {
          if (start != -1) {
            numbers = numbers :+ Number(
              lineIdx,
              start,
              charIdx - start,
              matrix(lineIdx).toList.slice(start, charIdx).mkString("").toInt
            )
            start = -1
          }
        }
      }
      if (start != -1) {
        numbers = numbers :+ Number(
          lineIdx,
          start,
          lines(lineIdx).length() - start,
          matrix(lineIdx).toList
            .slice(start, lines(lineIdx).length())
            .mkString("")
            .toInt
        )
      }
    }
    println(matrix.toList.map(_.toList))
    println(numbers)
    numbers.foreach(n => println(s"${n}: ${n.isValid(matrix)}"))
    numbers.filter(_.isValid(matrix)).map(_.value).reduce((x, y) => x + y)

    // val matrix = Array(Array[Char]())

    // 0
  }

  override def part2(input: String): Int = ???

}
