from functools import reduce

def parse_input(debug=False):
    filename = 'test.txt' if debug else '6.txt'
    with open(f'input/{filename}', 'r') as f:
        return f.read().strip()

def chars_until_unique(data, num_distinct):
    last = list(data[:num_distinct])
    idx = 4
    while len(set(last)) != num_distinct:
        last.pop(0)
        last.append(data[idx])
        idx += 1
    return idx

def part1():
    data = parse_input()
    return chars_until_unique(data, 4)

def part2():
    data = parse_input()
    return chars_until_unique(data, 14)

print(part1())
print(part2())
