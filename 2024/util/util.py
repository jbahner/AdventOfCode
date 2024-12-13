import inspect
import os
import urllib.request
from dotenv import find_dotenv
from dotenv import load_dotenv
from enum import Enum


class Direction(Enum):
    NORTH = -1, 0
    EAST = 0, 1
    SOUTH = 1, 0
    WEST = 0, -1

    def add(self, cell):
        return cell[0] + self.value[0], cell[1] + self.value[1]


def in_bounds(row, col, array2d):
    return 0 <= row < len(array2d) and 0 <= col < len(array2d[row])


def download_file(local_path):
    env_file = find_dotenv(".env")
    load_dotenv(env_file)
    token = os.getenv('AOC_TOKEN')
    year = local_path.rsplit(os.sep)[-2]
    day = int((local_path.rsplit(os.sep)[-1])[-2:])
    assert token is not None and len(year) == 4 and day is not None

    r = urllib.request.Request(f'https://adventofcode.com/{year}/day/{day}/input')
    r.add_header("Cookie", f'session={token}')
    content = urllib.request.urlopen(r).read().decode()
    with open(f'{local_path}/input.txt', 'w') as file:
        file.write(content)


def load(path, test=False):
    input_file = f"{path}/{'test_' if test else ''}input.txt"
    if not test and not os.path.isfile(input_file):
        download_file(path)
    return [line.rstrip() for line in open(input_file, "r", encoding="utf-8")]


def load_input(test=False):
    path = os.path.dirname((inspect.stack()[1])[1])
    return load(path, test)


def load_grid(test=False):
    path = os.path.dirname((inspect.stack()[1])[1])
    return [list(line) for line in load(path, test=test)]
