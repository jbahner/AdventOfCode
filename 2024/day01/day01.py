from util import *
import re


def part1(list1, list2):
    list1 = sorted(list1)
    list2 = sorted(list2)
    res = 0
    for i in range(len(list1)):
        res += abs(list1[i] - list2[i])
    print('part 1', res)


def part2(list1, list2):
    counts = dict()

    for num in list2:
        counts[num] = counts.get(num, 0) + 1
    res = 0

    for num in list1:
        res += num * counts.get(num, 0)

    print('part 2', res)


def main():
    lines = load_input()
    list1 = []
    list2 = []
    for line in lines:
        splitted = re.split('\\s+', line.rstrip())
        list1.append(int(splitted[0]))
        list2.append(int(splitted[1]))
    part1(list1, list2)
    part2(list1, list2)


main()
