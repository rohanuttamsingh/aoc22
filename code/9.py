from collections.abc import Hashable
from functools import reduce

class Coords(Hashable):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Coords(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Coords(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f'({self.x}, {self.y})'

    def __hash__(self):
        return hash((self.x, self.y))

def parse_input(debug):
    with open(f"input/{'test' if debug else '9'}.txt", 'r') as f:
        raw = f.read().split('\n')[:-1]
    dir_map = {'R': (0, 1), 'L': (0, -1), 'U': (1, 0), 'D': (-1, 0)}
    lines_raw = map(lambda x: x.split(' '), raw)
    motions_raw = [(line[0], int(line[1])) for line in lines_raw]
    motions = reduce(
        lambda x, y : x + y,
        [[dir_map[motion[0]]] * motion[1] for motion in motions_raw]
    )
    motions = list(map(lambda a: Coords(a[0], a[1]), motions))
    return motions

def touching(head_coords, tail_coords):
    diff = head_coords - tail_coords
    return abs(diff.x) <= 1 and abs(diff.y) <= 1

def get_tail_coords(head_coords, tail_coords):
    diff = head_coords - tail_coords
    if touching(head_coords, tail_coords):
        return tail_coords

    new_coords = tail_coords

    # Same row or col
    if diff.x == 0:
        new_coords += Coords(0, diff.y // 2)
    elif diff.y == 0:
        new_coords += Coords(diff.x // 2, 0)

    # Knight shaped
    elif abs(diff.x) == 1:
        new_coords += Coords(diff.x, diff.y // 2)
    elif abs(diff.y == 1):
        new_coords += Coords(diff.x // 2, diff.y)
    
    # 2-space diagonal
    else:
        new_coords += Coords(diff.x // 2, diff.y // 2)

    return new_coords

def part1(debug=False):
    moves = parse_input(debug)
    head_coords = Coords(0, 0)
    tail_coords = Coords(0, 0)
    visited = set()
    for move in moves:
        head_coords += move
        tail_coords = get_tail_coords(head_coords, tail_coords)
        visited.add(tail_coords)
    return len(visited)

def part2(debug=False):
    moves = parse_input(debug)
    knots = [Coords(0, 0)] * 10
    visited = set()
    for move in moves:
        knots[0] += move
        for i in range(1, len(knots)):
            knots[i] = get_tail_coords(knots[i - 1], knots[i])
        visited.add(knots[-1])
    return len(visited)

print(part1())
print(part2())
