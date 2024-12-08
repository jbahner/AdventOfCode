from util import *


def add(a, b):
    return a + b


def mult(a, b):
    return a * b


def try_combinations(nums, operations):
    if len(nums) == 2:
        return nums[0] == nums[1]
    cur = nums[0]
    a = nums[1]
    b = nums[2]
    remaining_nums = nums[3:]
    for operation in operations:
        if try_combinations([cur, operation(a, b)] + remaining_nums, operations):
            return cur
    return 0


def part1(lines):
    result = 0
    for line in lines:
        nums = list(map(int, line.replace(':', '').split()))
        result += try_combinations(nums, [add, mult])
    print(result)


def concat(a, b):
    return int(f"{a}{b}")


def part2(lines):
    result = 0
    for line in lines:
        nums = list(map(int, line.replace(':', '').split()))
        result += try_combinations(nums, [add, mult, concat])
    print(result)


def main():
    lines = load_input()
    part1(lines)
    part2(lines)


main()
