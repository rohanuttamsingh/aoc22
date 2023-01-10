import json

def parse_input(debug):
    with open(f"input/{'test' if debug else '13'}.txt", 'r') as f:
        raw = f.read().strip().split('\n\n')
    pairs = [pair.split('\n') for pair in raw]
    pairs = [[json.loads(pair[0]), json.loads(pair[1])] for pair in pairs]
    return pairs

def compare(left, right):
    if len(left) == 0:
        return 0
    if len(right) == 0:
        return 1
    head_left, *tail_left = left
    head_right, *tail_right = right
    if type(head_left) == int and type(head_right) == int:
        if head_left < head_right:
            return 0
        if head_left > head_right:
            return 1
        return compare(tail_left, tail_right)
    elif type(head_left) == list and type(head_right) == list:
        res = compare(head_left, head_right)
        if res == 2:
            return compare(tail_left, tail_right)
        return res
    elif type(head_left) == int:
        head_left = [head_left]
    elif type(head_right) == int:
        head_right = [head_right]
    res = compare(head_left, head_right)
    if res == 2:
        return compare(tail_left, tail_right)
    return res

def part1(debug=False):
    pairs = parse_input(debug)
    comps = [compare(pair[0], pair[1]) for pair in pairs]
    print(comps)
    total = 0
    for i, comp in enumerate(comps):
        if comp != 1:
            total += i + 1
    return total

print(part1())
