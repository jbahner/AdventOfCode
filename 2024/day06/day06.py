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


def part2(lines):
    sum = 0
    start_x,start_y = None, None
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == '^':
                start_x = i
                start_y = j
                sum += 1
                # lines[i][j] = 'X'
    if start_x is None or start_y is None:
        print('not found')
        exit(1)
    # for line in lines:
    #     print(''.join(line))
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            with_obstacle = copy.deepcopy(lines)
            with_obstacle[i][j] = '0'
            direction = Direction.NORTH
            visited = dict()
            x = start_x
            y = start_y
            while True:
                x_offset, y_offset = direction.value
                if x + x_offset < 0 or x + x_offset >= len(with_obstacle[0]) or y + y_offset < 0 or y + y_offset >= len(with_obstacle):
                    break
                if with_obstacle[x + x_offset][y + y_offset] in ['#', '0']:
                    direction = ninety_degrees(direction)
                    with_obstacle[x][y] = '+'
                    continue
                x = x + x_offset
                y = y + y_offset
                if x < 0 or x >= len(with_obstacle[0]) or y < 0 or y >= len(with_obstacle):
                    break
                visited[(x,y)] = visited.setdefault((x, y), 0) + 1
                if with_obstacle[x][y] != '^':
                    if direction == Direction.NORTH or direction == Direction.SOUTH:
                        with_obstacle[x][y] = '|' if with_obstacle[x][y] != '-' else '+'
                    else:
                        with_obstacle[x][y] = '-' if with_obstacle[x][y] != '|' else '+'
                    # with_obstacle[x][y] = direction == North'X'
                f = len([v for k, v in visited.items() if v > 3])
                if f >= 5:
                    sum += 1
                    print()
                    print()
                    print()
                    for line in with_obstacle:
                        print(''.join(line))
                    break
            # print()
            # print()
            # print()
            # for line in with_obstacle:
            #     print(''.join(line))
# todo nur letzte 4 abzweigungen merken und schauen ob gleiches y bzw x

    print(sum)

def part2_test(lines):
    sum = 0
    start_x,start_y = None, None
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == '^':
                start_x = i
                start_y = j
                sum += 1
                # lines[i][j] = 'X'
    if start_x is None or start_y is None:
        print('not found')
        exit(1)
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == '#':
                continue
            with_obstacle = copy.deepcopy(lines)
            with_obstacle[i][j] = '0'
            direction = Direction.NORTH
            x = start_x
            y = start_y
            steps = []
            times_at_start = -1
            turns_for_first = []
            turns_for_second = []
            while True:
                if i == 8 and j == 3:
                    print()
                    print()
                    print()
                    print(x, y)

                    for iidx in range(len(with_obstacle)):
                        print(iidx, ''.join(with_obstacle[iidx]))
                x_offset, y_offset = direction.value
                if x + x_offset < 0 or x + x_offset >= len(with_obstacle[0]) or y + y_offset < 0 or y + y_offset >= len(with_obstacle):
                    break
                if with_obstacle[x + x_offset][y + y_offset] in ['#', '0']:
                    direction = ninety_degrees(direction)
                    with_obstacle[x][y] = '+'
                    # if times_at_start == 1:
                    #     turns_for_first.append((x, y))
                    # elif times_at_start == 2:
                    #     turns_for_second.append((x, y))
                    continue
                x = x + x_offset
                y = y + y_offset
                if x == start_x and y == start_y:
                    times_at_start += 1
                if times_at_start > 1:
                    if steps[0] == steps[1]:
                        sum += 1
                    break
                if times_at_start >= 0 and x == start_x and y == start_y:
                    if len(steps) < (times_at_start + 1):
                        steps.append(0)
                    steps[times_at_start] = steps[times_at_start] + 1

                # if times_at_start >= 0:
                #     if len(steps) < (times_at_start + 1):
                #         steps.append(0)
                #     steps[times_at_start] = steps[times_at_start] + 1
                # if x == start_x and y == start_y:
                #         times_at_start += 1
                #         if times_at_start > 2:
                #             if steps[0] == steps[1]:
                #                 sum += 1
                #             break

            # if with_obstacle[x][y] != '^':
                #     if direction == Direction.NORTH or direction == Direction.SOUTH:
                #         with_obstacle[x][y] = '|' if with_obstacle[x][y] != '-' else '+'
                #     else:
                #         with_obstacle[x][y] = '-' if with_obstacle[x][y] != '|' else '+'


def main():
    lines = load_input()
    lines = [list(arr) for arr in lines]
    # part1(lines)
    # part2(lines)
    part2_test(lines)

main()