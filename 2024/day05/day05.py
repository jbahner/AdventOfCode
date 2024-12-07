from functools import cmp_to_key
from util import *

def read_file():
    with open('input.txt') as file:
        entire_file = file.read()
        parts = entire_file.split('\n\n')
        return parts[0].split('\n'), parts[1].split('\n')

# todo a bit prettier
def part1(rules, updates):
    order = dict()
    for rule in rules:
        before, after = rule.split('|')
        order.setdefault(before, []).append(after)
    sum = 0
    for update in updates:
        pages = update.split(',')
        valid = True
        for i in reversed(range(len(pages))):
            pages_after = order.get(pages[i])
            if pages_after is None:
                continue
            if any(p in pages_after for p in pages[:i]):
                valid = False
        if valid:
            sum += int(pages[int((len(pages) - 1) / 2)])
    print(sum)

def cmp(u1, u2, order_map):
    u1_after = order_map.get(u1, [])
    u2_after = order_map.get(u2, [])
    if u2 in u1_after:
        return -1
    if u1 in u2_after:
        return 1
    return 0


def part2(rules, updates):
    order = dict()
    for rule in rules:
        before, after = rule.split('|')
        order.setdefault(before, []).append(after)
    sum = 0
    for update in updates:
        pages = update.split(',')
        sorted_pages = sorted(pages, key= cmp_to_key(lambda u1, u2: cmp(u1, u2, order)))
        if any(a != b for a, b in zip(sorted_pages, pages)):
            sum += int(sorted_pages[int((len(sorted_pages) - 1) / 2)])
    print(sum)

def main():
    (rules, updates) = read_file()
    part1(rules, updates)
    part2(rules, updates)


main()