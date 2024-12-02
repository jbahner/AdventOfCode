package jbahner.aoc

object Day04 extends AoCSolution {

  case class Card(id: Int, winning: Array[String], chosen: Array[String]) {
    lazy val calculatePoints: Int = chosen
      .filter(winning.contains(_))
      .foldLeft(0)((prod, _) => if (prod == 0) 1 else prod * 2)

    lazy val numberOfWins: Int = chosen.filter(winning.contains(_)).size

    lazy val isWin: Boolean = winning.exists(chosen.contains)
  }

  override def part1(input: String): Int = {
    input
      .split("\n")
      .map(line => {
        val splitted = line.split(":")
        val cardId = splitted(0).split("\\s+")(1).toInt
        val parts = splitted(1).trim().split("\\|")
        Card(
          cardId,
          parts(0).split("\\s+"),
          parts(1).split("\\s+")
        ).calculatePoints
      })
      .reduce((sum, points) => sum + points)
  }

  override def part2(input: String): Int = {
    val cards = input
      .split("\n")
      .map(line => {
        val splitted = line.split(":")
        val cardId = splitted(0).split("\\s+")(1).toInt
        val parts = splitted(1).trim().split("\\|")
        Card(
          cardId,
          parts(0).split("\\s+"),
          parts(1).split("\\s+")
        )
      })
    val numCopies = Array.fill(cards.size)(1)
    while (numCopies.exists(_ > 0)) {}

    calculateCards(0, cards)
  }

  def calculateCards(id: Int, cards: Array[Card]): Int = {
    // val isWin = cards(id).numberOfWins
    // if (id > 100) System.exit(1)
    if (id >= cards.length) {
      println(s"Exiting at ${id}")
      return 0
    }
    println(s"In card: ${id}")
    println(cards(id).numberOfWins)
    println(cards(id).numberOfWins + id)
    var sum = 1
    if (cards(id).numberOfWins > 0) {
      for (i <- id + 1 to id + cards(id).numberOfWins) {
        println(i)
        sum += calculateCards(i, cards)
      }
    }
    sum + calculateCards(id + 1, cards)
    // 1 + cards(id).numberOfWins + calculateCards(id + 1, cards)
    // println(id)
    // var sum = 0
    // println("Additional:")
    // for (i <- id to id + cards(id).numberOfWins) {
    // if (i < cards.length && cards(i).isWin) sum += 1
    // }
    // sum + calculatePoints(id + 1, cards)
  }

  // def calculateOnlyNext()

}
