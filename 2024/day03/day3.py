import re
def read_file():
    with open('input.txt') as file:
        return file.read()

def part1(content):
    pattern = re.compile(r'mul\((\d{1,3})\,(\d{1,3})\)')
    sum = 0
    for n1, n2 in re.findall(pattern, content):
        sum += int(n1) * int(n2)
    print(sum)

def part2(content):
    do_mul = True
    pattern = re.compile(r'mul\((\d{1,3})\,(\d{1,3})\)')
    sum = 0
    for m in re.finditer(pattern, content):
        do_idx = content[0:m.start()].rfind('do()')
        dont_idx = content[0:m.start()].rfind('don\'t()')
        if do_idx != -1 or dont_idx != -1:
            if (max(do_idx, 0) - max(dont_idx, 0)) > 0:
                do_mul = True
            else:
                do_mul = False
        n1, n2 = m.groups()
        if do_mul:
            sum += int(n1) * int(n2)
    print(sum)

content = read_file()
part1(content)
part2(content)