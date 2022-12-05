from functools import reduce

def parse_input_1():
    with open('input/3.txt', 'r') as f:
        raw = f.read().split('\n')[:-1]
    comp1s, comp2s = [], []
    for sack in raw:
        mid = len(sack) // 2
        comp1s.append(sack[:mid])
        comp2s.append(sack[mid:])
    return comp1s, comp2s

def parse_input_2():
    with open('input/3.txt', 'r') as f:
        raw = f.read().split('\n')[:-1]
    groups = []
    for i in range(0, len(raw), 3):
        groups.append([raw[i]] + [raw[i + 1]] + [raw[i + 2]])
    return groups

def get_priority(letter):
    val = ord(letter)
    if val <= ord('Z'):
        return val - ord('A') + 27
    return val - ord('a') + 1

def part1():
    comp1s, comp2s = parse_input_1()
    return sum([get_priority(list(set(comp1) & set(comp2))[0]) for comp1, comp2 in zip(comp1s, comp2s)])

def part2():
    groups = parse_input_2()
    return sum([get_priority(list(reduce(lambda a, b: set(a) & set(b), group))[0]) for group in groups])

print(part1())
print(part2())
