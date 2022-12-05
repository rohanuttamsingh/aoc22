def intervals_to_endpoints(pair):
    int1, int2 = pair
    convert = lambda int_: list(map(int, int_.split('-')))
    int1, int2 = convert(int1), convert(int2)
    return [int1, int2]

def parse_pairs():
    with open('input/4.txt', 'r') as f:
        raw = f.read().split('\n')[:-1]
    pairs_raw = [line.split(',') for line in raw]
    pairs = [intervals_to_endpoints(pair) for pair in pairs_raw]
    return pairs

def contained(pair):
    int1, int2 = pair
    contains = lambda x, y: x[0] <= y[0] and x[1] >= y[1]
    return contains(int1, int2) or contains(int2, int1)

def overlaps(pair):
    int1, int2 = pair
    if int2[0] < int1[0]:
        int1, int2 = int2, int1
    return int1[1] >= int2[0]

def part1():
    pairs = parse_pairs()
    return sum([int(contained(pair)) for pair in pairs])

def part2():
    pairs = parse_pairs()
    return sum([int(overlaps(pair)) for pair in pairs])

print(part1())
print(part2())
