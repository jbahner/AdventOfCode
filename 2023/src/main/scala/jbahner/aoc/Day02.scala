package jbahner.aoc
import scalaz.*, Scalaz.*

object Day02 extends AoCSolution {

  case class GameConfig(red: Int, green: Int, blue: Int) {
    def isPossible(redMax: Int, greenMax: Int, blueMax: Int): Boolean =
      red <= redMax && green <= greenMax && blue <= blueMax
  }

  case class Game(configs: Array[GameConfig]) {
    def isPossible(redMax: Int, greenMax: Int, blueMax: Int): Boolean =
      configs.forall(_.isPossible(redMax, greenMax, blueMax))
  }

  def colorToTriple(singleColor: String): (Int, Int, Int) =
    singleColor.split(" ") match
      case Array(n, "red")   => (n.toInt, 0, 0)
      case Array(n, "green") => (0, n.toInt, 0)
      case Array(n, "blue")  => (0, 0, n.toInt)

  def parseGame(game: String): Game = {
    Game(
      game
        .split(";")
        .map(set =>
          val colors = set
            .split(",")
            .map(s => colorToTriple(s.trim()))
            .foldLeft((0, 0, 0))((cur, triple) => cur |+| triple)
          GameConfig(colors._1, colors._2, colors._3)
        )
    )
  }

  override def part1(input: String): Int = {
    val redMax = 12
    val greenMax = 13
    val blueMax = 14
    input
      .split("\n")
      .map(line => {
        val splitted = line.split(":")
        (splitted(0).split(" ")(1).toInt, parseGame(splitted(1)))
      })
      .filter((id, game) => {
        println(id); game.isPossible(redMax, greenMax, blueMax)
      })
      .map(_._1)
      .reduce((sum, id) => sum + id)
  }

  override def part2(input: String): Int = ???

}
