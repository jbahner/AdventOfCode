import inspect
import os


def load_input(test = False):
    path = os.path.dirname((inspect.stack()[1])[1])
    return [line.rstrip() for line in open(f"{path}/{'test_' if test else ''}input.txt", "r", encoding="utf-8")]
