from util import *
from enum import Enum


class Side:
    def __init__(self, orientation, cell):
        self.orientation = orientation
        self.position = cell[1] if orientation == Orientation.Vertical else cell[0]
        self.start = cell[1] if self.position == cell[0] else cell[1]
        self.end = self.start

    def __str__(self):
        return f'orientation={self.orientation}, position={self.position} start={self.start}, end={self.end}'

    def add_if(self, cell):
        if not self.is_same_vector(cell):
            return False
        location = cell[0] if self.orientation == Orientation.Vertical else cell[1]
        if location - 1 == self.end:
            self.end = location
            return True
        elif location + 1 == self.start:
            self.start = location
            return True
        return False

    def is_same_vector(self, cell):
        return self.position == (cell[1] if self.orientation == Orientation.Vertical else cell[0])



class Orientation(Enum):
    Vertical = -1, 0
    Horizontal = 0, -1

    @staticmethod
    def from_direction(direction: Direction):
        return Orientation.Vertical if direction in [Direction.NORTH, Direction.SOUTH] else Orientation.Horizontal


class Strategy(Enum):
    Perimeter = 0
    Sides = 1

    def execute(self, region):
        if self == Strategy.Perimeter:
            return region.perimeter()
        else:
            return region.sides()


def neighbors(cell1, cell2):
    if abs(cell1[0] - cell2[0]) == 1 and cell1[1] == cell2[1]:
        return Orientation.Vertical
    elif cell1[0] == cell1[0] and abs(cell1[1] - cell2[1]) == 1:
        return Orientation.Horizontal
    else:
        return None


class Region:
    def __init__(self, identifier):
        self.identifier = identifier
        self.cells = set()

    def __str__(self):
        return f'id={self.identifier}, cells={", ".join([f"[{cell}]" for cell in self.cells])}'

    def adjacent(self, row, col):
        for (r, c) in self.cells:
            for d in Direction:
                (row_off, col_off) = d.value
                if r + row_off == row and c + col_off == col:
                    return True
        return False

    def price(self, strategy: Strategy):
        return strategy.execute(self) * len(self.cells)

    def perimeter(self):
        perimeter = 0
        for (row, col) in self.cells:
            for d in Direction:
                (row_off, col_off) = d.value
                if (row + row_off, col + col_off) not in self.cells:
                    perimeter += 1
        return perimeter

    def sides(self):
        sides = set()
        # sides = dict()
        self.cells = sorted(self.cells, key=lambda x: (x[0], x[1]))
        for cell in self.cells:
            for d in Direction:
                added = False
                orientation = Orientation.from_direction(d)
                for side in filter(lambda s: s.orientation == orientation, sides):
                    if side.add_if(cell):
                        added = True
                if not added:
                    sides.add(Side(orientation, cell))
        print(self)
        for side in sides:
            print(side)
        print()
        return len(sides)


def assign_region(regions, id, row, col):
    adjacent_regions_with_id = [region for region in regions if region.identifier == id and region.adjacent(row, col)]
    if len(adjacent_regions_with_id) == 0:
        region = Region(id)
        regions.add(region)
    elif len(adjacent_regions_with_id) > 1:
        # Merge regions this cell connects to each other
        region = adjacent_regions_with_id[0]
        for i in range(1, len(adjacent_regions_with_id)):
            region.cells.update(adjacent_regions_with_id[i].cells)
            regions.remove(adjacent_regions_with_id[i])
    else:
        region = adjacent_regions_with_id[0]
    region.cells.add((row, col))


def create_regions(grid):
    regions = set()
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            assign_region(regions, grid[row][col], row, col)
    return regions


def part1(grid):
    print(sum([r.price(Strategy.Perimeter) for r in create_regions(grid)]))


#
def part2(grid):
    print(sum([r.price(Strategy.Sides) for r in create_regions(grid)]))


def main():
    grid = load_grid(True)
    # part1(grid)
    part2(grid)


main()
