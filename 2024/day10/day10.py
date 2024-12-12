from util import load_grid, in_bounds

def valid_step(row, col, topo, prev):
    return topo[row][col] == prev + 1

def test_path(topo, y, x, visited=None):
    if visited is not None and (y, x) in visited:
        return 0
    if visited is not None:
        visited.add((y, x))
    if topo[y][x] == 9:
        return 1
    score = 0
    for row, col in [(y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)]:
        if in_bounds(row, col, topo) and valid_step(row, col, topo, topo[y][x]):
            score += test_path(topo, row, col, visited)
    return score

def part1(topo):
    total_score = 0
    for row in range(len(topo)):
        for col in range(len(topo[row])):
            if topo[row][col] == 0:
                visited = set()
                total_score += test_path(topo, row, col, visited)

    print(total_score)

def part2(topo):
    total_rating = 0
    for row in range(len(topo)):
        for col in range(len(topo[row])):
            if topo[row][col] == 0:
                total_rating += test_path(topo, row, col)
    print(total_rating)

def main():
    input = [[int(cell) for cell in rows] for rows in load_grid()]
    print(input)
    for line in input:
        print(''.join([str(c) for c in line]))
    part1(input)
    part2(input)

main()
