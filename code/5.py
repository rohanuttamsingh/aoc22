def parse_crates(crates_raw):
    num_crates = (len(crates_raw[0]) + 1) // 4
    crates = ['' for _ in range(num_crates)]
    for level in crates_raw[::-1]:
        for crate_num in range(num_crates):
            crate_letter = level[4 * crate_num + 1]
            if crate_letter != ' ':
                crates[crate_num] += crate_letter
    return crates

def parse_moves(moves_raw):
    moves = []
    for line in moves_raw:
        split = line.split(' ')
        item = lambda i, sub: int(split[i]) - sub
        amt, src, dest = item(1, 0), item(3, 1), item(5, 1)
        moves.append((amt, src, dest))
    return moves

def parse_input(debug=False):
    filename = 'test.txt' if debug else '5.txt'
    with open(f'input/{filename}', 'r') as f:
        raw = f.read().split('\n')[:-1]
    split_idx = raw.index('')
    crates_raw = raw[:split_idx - 1]
    moves_raw = raw[split_idx + 1:]
    crates = parse_crates(crates_raw)
    moves = parse_moves(moves_raw)
    return crates, moves

def process_move(crates, move, rev):
    amt, src, dest = move
    moving = crates[src][-amt:]
    if rev:
        moving = moving[::-1]
    crates[src] = crates[src][:-amt]
    crates[dest] += moving

def process_all_moves(crates, moves, rev):
    for move in moves:
        process_move(crates, move, rev)
    return ''.join([crate[-1] for crate in crates])

def part1():
    crates, moves = parse_input()
    return process_all_moves(crates, moves, True)

def part2():
    crates, moves = parse_input()
    return process_all_moves(crates, moves, False)

print(part1())
print(part2())
