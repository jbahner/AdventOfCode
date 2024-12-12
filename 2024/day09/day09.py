from util import load_input


class Area:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.size = self.end - self.start


def get_blocks(diskmap):
    blocks = []
    cur_block = 0
    for i in range(len(diskmap)):
        if i % 2 == 0:
            blocks.extend([str(cur_block)] * int(diskmap[i]))
            cur_block += 1
        else:
            blocks.extend(['.'] * int(diskmap[i]))
    return blocks


def checksum(blocks):
    total = 0
    for i in range(len(blocks)):
        if blocks[i] == '.':
            continue
        total += int(blocks[i]) * i
    return total


def part1(blocks):
    left = 0
    right = len(blocks)
    while any((c != '.' for c in block) for block in blocks[left:right]):
        if blocks[left] != '.':
            left += 1
            continue
        if blocks[right - 1] == '.':
            right -= 1
            continue
        blocks[left] = blocks[right - 1]
        blocks[right - 1] = '.'
    # print(''.join(blocks))
    print(checksum(blocks))


def swap(empty_space, used_space, blocks):
    for i in range(used_space.size):
        assert blocks[empty_space.start + i] == '.'
        assert blocks[used_space.start + i] != '.'
        blocks[empty_space.start + i] = blocks[used_space.start + i]
        blocks[used_space.start + i] = '.'


def part2(blocks):
    print(''.join(blocks))
    free_spaces = list()
    in_free_space = False
    space_start = None
    for i in range(len(blocks)):
        if blocks[i] == '.':
            if not in_free_space:
                space_start = i
                in_free_space = True
        else:
            if in_free_space:
                free_spaces.append(Area(space_start, i))
                in_free_space = False
    if in_free_space:
        free_spaces.append(Area(space_start, len(blocks)))

    used_spaces = list()
    cur = None
    space_start = None
    for i in range(len(blocks)):
        if blocks[i] != '.':
            if cur is None or blocks[i] != cur:
                if space_start is not None:
                    used_spaces.append(Area(space_start, i))
                space_start = i
                cur = blocks[i]
        else:
            if space_start is not None:
                used_spaces.append(Area(space_start, i))
                space_start = None
                cur = None

    if space_start is not None:
        used_spaces.append(Area(space_start, len(blocks)))

    for used_space in reversed(used_spaces):
        for i, free_space in enumerate(free_spaces):
            if free_space.size >= used_space.size:
                swap(free_space, used_space, blocks)
                if free_space.size > used_space.size:
                    free_spaces[i] = Area(free_space.start + used_space.size, free_space.end)
                else:
                    free_spaces.pop(i)
                break

    print(checksum(blocks))


def main():
    diskmap = load_input()[0]
    # part1(get_blocks(diskmap))
    part2(get_blocks(diskmap))


main()
