import os
import sys
sys.path.insert(1, f'{os.getcwd()}/2024')

from util import *
import re
list1 = []
list2 = []

lines = load_input()
for line in lines:
    splitted = re.split('\\s+', line.rstrip())
    list1.append(int(splitted[0]))
    list2.append(int(splitted[1]))
sum = 0
list1 = sorted(list1)
list2 = sorted(list2)
for i in range(len(list1)):
    sum += abs(list1[i] - list2[i])
print(sum)
