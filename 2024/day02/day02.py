import os
import sys
sys.path.insert(1, f'{os.getcwd()}/2024')

from util import *

def check_line(line):
    levels = [int(x) for x in line.split()]
    increasing = (levels[1] - levels[0]) > 0
    for i in range(1, len(levels)):
        comp = levels[i] - levels[i-1]
        if abs(comp) < 1 or abs(comp) > 3 or (increasing and comp <= 0) or (not increasing and comp >= 0):
            return False
    return True

lines = load_input()
num_safe = 0
for line in lines:
    if check_line(line):
        num_safe += 1

print(num_safe)