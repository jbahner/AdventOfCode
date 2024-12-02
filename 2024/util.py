import inspect
import os


def load_input(test = False):
    # filename = f'2024/day{day}/{'test_' if test else ''}input.txt' 
    path = os.path.dirname((inspect.stack()[1])[1])
    return [line.rstrip() for line in open(f'{path}/{'test_' if test else ''}input.txt')]
    # with open(f'{path}/{'test_' if test else ''}input.txt') as file:
        # return file.read()

