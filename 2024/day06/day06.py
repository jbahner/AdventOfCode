from enum import Enum
import copy
from util import *

class Direction(Enum):
    NORTH = -1, 0
    EAST = 0, 1
    SOUTH = 1, 0
    WEST = 0, -1

def ninety_degrees(direction):
    if direction == Direction.NORTH:
        return Direction.EAST
    elif direction == Direction.EAST:
        return Direction.SOUTH
    elif direction == Direction.SOUTH:
        return Direction.WEST
    else:
        return Direction.NORTH


def part1(lines):
    sum = 0
    x, y = None, None
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == '^':
                x = i
                y = j
                sum += 1
                lines[i][j] = 'X'
    if x is None or y is None:
        print('not found')
        exit(1)
    direction = Direction.NORTH
    while True:
        x_offset, y_offset = direction.value
        if x + x_offset < 0 or x + x_offset >= len(lines[0]) or y + y_offset < 0 or y + y_offset >= len(lines):
            break
        if lines[x + x_offset][y + y_offset] == '#':
            direction = ninety_degrees(direction)
            continue
        x = x + x_offset
        y = y + y_offset
        if x < 0 or x >= len(lines[0]) or y < 0 or y >= len(lines):
            break
        if lines[x][y] != 'X':
            sum += 1
        lines[x][y] = 'X'
    for line in lines:
        print(''.join(line))
    print(sum)



def main():
    lines = load_input()
    lines = [list(arr) for arr in lines]
    part1(lines)

main()