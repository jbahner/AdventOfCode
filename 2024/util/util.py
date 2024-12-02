import inspect
import os


def load_input(test=False, part=None):
    path = os.path.dirname((inspect.stack()[1])[1])
    return [line.rstrip() for line in open(f"{path}/{'test_' if test else ''}input{'' if part is None else f'_part{part}'}.txt", "r", encoding="utf-8")]
