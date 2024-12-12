from util import load_grid
from util import Direction
from enum import Enum

class Orientation(Enum):
    Vertical = 0
    Horizontal = 1

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
        return f'id={self.identifier}, cells={', '.join([f'[{cell}]' for cell in self.cells])}'

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
        sides = dict()
        for (row, col) in self.cells:
            for cell in self.cells:
                if cell == (row, col):
                    continue
                orientation = neighbors((row, col), cell)
                if orientation == Orientation.Horizontal:
                    ## Increment dict at col + Orientation

                elif orientation == Orientation.Vertical:
                    #other

def assign_region(regions, id, row, col):
    adjacent_regions_with_id = [region for region in regions if region.identifier == id and region.adjacent(row, col)]
    if len(adjacent_regions_with_id) == 0:
        region = Region(id)
        regions.add(region)
    elif len(adjacent_regions_with_id) > 1:
        # Merge regions this cell connects to
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
# def part2(grid):
#     print(sum([r.price() for r in create_regions(grid)]))



def main():
    grid = load_grid()
    part1(grid)

main()