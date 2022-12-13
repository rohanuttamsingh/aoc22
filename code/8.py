from functools import reduce
import numpy as np

def parse_input(debug=False):
    with open(f"input/{'test' if debug else '8'}.txt", 'r') as f:
        raw = f.read().split('\n')[:-1]
    return np.array([list(map(int, list(raw_line))) for raw_line in raw])

def update_visible(trees, visible, axis, rowcol, forward):
    default = 0 if forward else trees.shape[(axis + 1) % 2] - 1
    highest_coords = tuple([rowcol if i == axis else default for i in range(2)])
    highest = trees[highest_coords]
    loop_range = range(1, trees.shape[(axis + 1) % 2] - 1) if forward else range(trees.shape[(axis + 1) % 2] - 2, 0, -1)
    for i in loop_range:
        tree_coords = tuple([rowcol if j == axis else i for j in range(2)])
        tree = trees[tree_coords]
        if tree > highest:
            visible[tree_coords] = 1
            highest = tree

def score_1_dir(trees, row, col, dir):
    height = trees[row, col]
    score = 0
    row += dir[0]
    col += dir[1]
    while row >= 0 and col >= 0 and row < trees.shape[0] and col < trees.shape[0]:
        score += 1
        if trees[row, col] >= height:
            break
        row += dir[0]
        col += dir[1]
    return score

def score_all_dirs(trees, row, col):
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    return reduce(lambda x, y: x * y, [score_1_dir(trees, row, col, dir) for dir in dirs])

def part1():
    trees = parse_input()
    visible = np.zeros_like(trees)
    for row in range(1, trees.shape[0] - 1):
        update_visible(trees, visible, 0, row, True)
        update_visible(trees, visible, 0, row, False)
    for col in range(1, trees.shape[1] - 1):
        update_visible(trees, visible, 1, col, True)
        update_visible(trees, visible, 1, col, False)
    return np.sum(visible, axis=None) + 2 * trees.shape[0] + 2 * trees.shape[1] - 4

def part2():
    trees = parse_input()
    scores = np.zeros_like(trees)
    for row in range(trees.shape[0]):
        for col in range(trees.shape[1]):
            scores[row, col] = score_all_dirs(trees, row, col)
    return np.max(scores, axis=None)

print(part1())
print(part2())
