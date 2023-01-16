from functools import reduce

def get_line(start, end):
    start_x, start_y = start
    end_x, end_y = end
    if start_x == end_x:
        return [(start_x, y) for y in range(min(start_y, end_y), max(start_y, end_y) + 1)]
    return [(x, start_y) for x in range(min(start_x, end_x), max(start_x, end_x) + 1)]

def get_lines(path):
    lines = []
    for i in range(len(path) - 1):
        lines.append(get_line(path[i], path[i + 1]))
    lines = reduce(lambda x, y: x + y, lines)
    return lines

def parse_input(debug):
    with open(f"input/{'test' if debug else '14'}.txt", 'r') as f:
        raw = f.read().strip().split('\n')
    paths = [line.split(' -> ') for line in raw]
    paths = [[(int(coords.split(',')[0]), int(coords.split(',')[1])) for coords in path] for path in paths]
    lines = [get_lines(path) for path in paths]
    occupied_squares = reduce(lambda x, y: x + y, lines)
    return occupied_squares

def construct_board(occupied_squares, min_x, max_x, max_y):
    board = [[0 for _ in range(min_x - 1, max_x + 2)] for _ in range(max_y + 1)]
    for x, y in occupied_squares:
        board[max_y - y][x - min_x + 1] = 1
    return board

def grain_fall(board, x, y, fall):
    if fall and (x == 0 or x == len(board[0]) - 1):
        return 'Fell'
    if board[y - 1][x] == 0:
        return grain_fall(board, x, y - 1, fall)
    if board[y - 1][x - 1] == 0:
        return grain_fall(board, x - 1, y - 1, fall)
    if board[y - 1][x + 1] == 0:
        return grain_fall(board, x + 1, y - 1, fall)
    return x, y

def part1(debug=False):
    occupied_squares = parse_input(debug)
    min_x = min(occupied_squares, key=lambda s: s[0])[0]
    max_x = max(occupied_squares, key=lambda s: s[0])[0]
    max_y = max(occupied_squares, key=lambda s: s[1])[1]
    board = construct_board(occupied_squares, min_x, max_x, max_y)
    grains = 0
    while True:
        new_pos = grain_fall(board, 500 - min_x + 1, max_y, True)
        if new_pos == 'Fell':
            return grains
        x, y = new_pos
        board[y][x] = 1
        grains += 1

def part2(debug=False):
    occupied_squares = parse_input(debug)
    min_x = min(occupied_squares, key=lambda s: s[0])[0]
    max_x = max(occupied_squares, key=lambda s: s[0])[0]
    max_y = max(occupied_squares, key=lambda s: s[1])[1]
    # In worst case, triangle with width equal to twice its height is required to get sand at (500, 0)
    max_y += 2
    for x in range(500 - max_y - 1, 500 + max_y + 1):
        occupied_squares.append((x, max_y))
    min_x = min(occupied_squares, key=lambda s: s[0])[0]
    max_x = max(occupied_squares, key=lambda s: s[0])[0]
    board = construct_board(occupied_squares, min_x, max_x, max_y)
    grains = 0
    while True:
        new_pos = grain_fall(board, 500 - min_x + 1, max_y, False)
        x, y = new_pos
        board[y][x] = 1
        grains += 1
        if new_pos == (500 - min_x + 1, max_y):
            return grains

print(part1())
print(part2())
