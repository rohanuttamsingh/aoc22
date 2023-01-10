import json
from enum import Enum

class Result(Enum):
    RIGHT = 1
    WRONG = 2
    INDETERMINATE = 3

def parse_input(debug):
    with open(f"input/{'test' if debug else '13'}.txt", 'r') as f:
        raw = f.read().strip().split('\n\n')
    pairs = [pair.split('\n') for pair in raw]
    pairs = [[json.loads(pair[0]), json.loads(pair[1])] for pair in pairs]
    return pairs

def compare_lists(l1, l2):
    if len(l1) == 0 and len(l2) == 0:
        return Result.RIGHT
    if len(l1) == 0 and len(l2) > 0:
        return Result.RIGHT
    if len(l1) > 0 and len(l2) == 0:
        return Result.WRONG
    head1, *tail1 = l1
    head2, *tail2 = l2
    if type(head1) == int and type(head2) == int:
        if head1 < head2:
            return Result.RIGHT
        elif head1 > head2:
            return Result.WRONG
        return compare_lists(tail1, tail2)
    elif type(head1) == int and type(head2) == list:
        return compare_lists([l1], l2)
    elif type(head1) == list and type(head2) == int:
        return compare_lists(l1, [l2])
    else:
        if len(head1) == 0 and len(head2) == 0:
            return Result.INDETERMINATE
        head_comp = compare_lists(head1, head2)
        if head_comp is not Result.INDETERMINATE:
            return head_comp
        return compare_lists(tail1, tail2)

def part1(debug=False):
    pairs = parse_input(debug)
    results = [compare_lists(pair[0], pair[1]) for pair in pairs]
    print(results)
    total = 0
    for i, result in enumerate(results):
        if result is Result.RIGHT or result is Result.INDETERMINATE:
            total += i + 1
    return total

print(part1())
