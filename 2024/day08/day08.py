from util import *
import itertools
import copy


def antenna_dict(lines):
    antennas = dict()
    for row in range(len(lines)):
        for col in range(len(lines[row])):
            if lines[row][col] != '.':
                antennas.setdefault(lines[row][col], []).append((row, col))
    return antennas


def in_bounds(row, col, lines):
    return 0 <= row < len(lines) and 0 <= col < len(lines)


def set_antinodes(row, col, lines):
    if in_bounds(row, col, lines):
        lines[row][col] = '#'


def part1(lines):
    antennas = antenna_dict(lines)
    for k, v in antennas.items():
        for (a1_row, a1_col), (a2_row, a2_col) in itertools.combinations(v, 2):
            row_off, col_off = (a1_row - a2_row, a1_col - a2_col)
            set_antinodes(a1_row + row_off, a1_col + col_off, lines)
            set_antinodes(a2_row + (row_off * -1), a2_col + (col_off * -1), lines)
    print(sum(line.count('#') for line in lines))


def set_antinodes_in_lines(antenna, direction, lines):
    row, col = antenna
    row_off, col_off = direction
    while in_bounds(row, col, lines):
        lines[row][col] = '#'
        row = row + row_off
        col = col + col_off


def part2(lines):
    antennas = antenna_dict(lines)
    for k, v in antennas.items():
        for a1, a2 in itertools.combinations(v, 2):
            direction = (a1[0] - a2[0], a1[1] - a2[1])
            set_antinodes_in_lines(a1, direction, lines)
            set_antinodes_in_lines(a2, [c * -1 for c in direction], lines)
    print(sum(line.count('#') for line in lines))


def main():
    lines = load_matrix()
    part1(copy.deepcopy(lines))
    part2(lines)


main()
