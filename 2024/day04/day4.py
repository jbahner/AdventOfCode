import re
from util import *

def directions(lines, y, x):
    x_min = max(0, x-1)
    x_max = min(len(lines[y]) - 1, x + 1)
    y_min = max(0, y - 1)
    y_max = min(len(lines) - 1, y + 1)
    dirs = []
    for i in range(y_min, y_max + 1):
        for j in range(x_min, x_max + 1):
            if lines[i][j] == 'M':
                dirs.append((i - y, j - x))
    return dirs

def part1(lines):
    sum = 0
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x] == 'X':
                dirs = directions(lines, y, x)
                for y_offset, x_offset in dirs:
                    if (y + (3 * y_offset)) < 0 or (y + (3 * y_offset)) >= len(lines) or (x + (3 * x_offset)) < 0 or  (x + (3 * x_offset)) >= len(lines[y]):
                        continue
                    if lines[y + (2* y_offset)][x + (2 * x_offset)] == 'A' and lines[y + (3 * y_offset)][x + (3 * x_offset)] == 'S':
                        sum +=1
    print(sum)

def check_mas(first, second):
    return first != second and 'S' in [first, second] and 'M' in [first, second]

def part2(lines):
    sum = 0
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x] == 'A':
                if y == 0 or y == len(lines) - 1 or x == 0 or x == len(lines[y]) - 1:
                    continue
                top_left = lines[y-1][x-1]
                bot_right = lines[y+1][x+1]
                top_right = lines[y-1][x+1]
                bot_left = lines[y+1][x-1]
                if check_mas(top_left, bot_right) and check_mas(top_right, bot_left):
                    sum += 1
    print(sum)

def main():
    lines = load_input()
    part1(lines)
    part2(lines)


main()