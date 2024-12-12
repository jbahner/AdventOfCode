from util import *

def solve(stone, blinks, res_map):
    if blinks == 0:
        return 1
    if (stone, blinks) in res_map:
        return res_map[(stone, blinks)]
    size = 0
    str_stone = str(stone)
    if stone == 0:
        size += solve(1, blinks - 1, res_map)
    elif len(str_stone) % 2 == 0:
        mid = len(str_stone) // 2
        size += solve(int(str_stone[:mid]), blinks - 1, res_map)
        size += solve(int(str_stone[mid:]), blinks - 1, res_map)
    else:
        size += solve(stone * 2024, blinks - 1, res_map)
    res_map[(stone, blinks)] = size
    return size


def solve_stones(stones, blinks):
    res_map = {}
    num_stones = 0
    for stone in stones:
        num_stones += solve(stone, blinks, res_map)
    print(num_stones)

def main():
    input = [int(num) for num in load_input()[0].split()]
    solve_stones(input, blinks=75)

main()