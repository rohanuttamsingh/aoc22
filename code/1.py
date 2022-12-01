import heapq

def parse():
    with open('input/1.txt', 'r') as f:
        raw = f.read()
    return raw[:-1].split('\n\n')

def part1():
    elves_raw = parse()
    max_cals = 0
    for elf_raw in elves_raw:
        lines = elf_raw.split('\n')
        cals = sum([int(line) for line in lines])
        max_cals = max(max_cals, cals)
    return max_cals

def part2():
    all_cals = []
    elves_raw = parse()
    for elf_raw in elves_raw:
        lines = elf_raw.split('\n')
        cals = sum([int(line) for line in lines])
        all_cals.append(cals)
    heapq.heapify(all_cals)
    return sum(heapq.nlargest(3, all_cals))

print(part1())
print(part2())
