lazy val root = project
  .in(file("."))
  .settings(
    name := "advent-of-code-2023",
    description := "Advent of Code 2023",
    version := "0.1.0",
    scalaVersion := "3.3.1",
    scalacOptions ++= Seq("-deprecation")
  )