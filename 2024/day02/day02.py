from util import *


def check_levels(levels):
    increasing = (levels[1] - levels[0]) > 0
    for i in range(1, len(levels)):
        comp = levels[i] - levels[i - 1]
        if abs(comp) < 1 or abs(comp) > 3 or (increasing and comp <= 0) or (not increasing and comp >= 0):
            return i
    return -1


def part1(lines_with_levels):
    num_safe = 0
    for levels in lines_with_levels:
        if check_levels(levels) < 0:
            num_safe += 1
    print(num_safe)


def check_replacement(levels, remove_idx):
    new_levels = levels[:remove_idx - 1] + levels[remove_idx:]
    return check_levels(new_levels) < 0


def part2(lines_with_levels):
    num_safe = 0
    for levels in lines_with_levels:
        failed_idx = check_levels(levels)
        if failed_idx > 0:
            if (not check_replacement(levels, failed_idx)
                    and not check_replacement(levels, failed_idx + 1)
                    and not check_replacement(levels, failed_idx - 1)):
                continue
            num_safe += 1
        else:
            num_safe += 1
    print(num_safe)


def main():
    lines = load_input()
    lines_with_levels = [[int(x) for x in line.split()] for line in lines]
    part1(lines_with_levels)
    part2(lines_with_levels)


main()
