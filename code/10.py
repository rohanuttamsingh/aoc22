from functools import reduce

def parse_input(debug):
    with open(f"input/{'test' if debug else '10'}.txt", 'r') as f:
        raw = f.read().split('\n')[:-1]
    mapping = lambda x: [0] if x == 'noop' else [0, int(x.split(' ')[1])]
    add_vals = list(map(mapping, raw))
    return reduce(lambda x, y: x + y, add_vals)

def part1(debug=False):
    add_vals = parse_input(debug)
    return sum([cycle * (1 + sum(add_vals[:cycle - 1])) for cycle in range(20, 221, 40)])

def part2(debug=False):
    add_vals = parse_input(debug)
    center_pos = [1]
    curr_pos = 1
    for add_val in add_vals:
        curr_pos += add_val
        center_pos.append(curr_pos)
    output = []
    for i in range(6):
        row = ''
        for j in range(40):
            if abs(center_pos[40 * i + j] - j) <= 1:
                row += '#'
            else:
                row += '.'
        output.append(row)
    return '\n'.join(output)

print(part1())
print(part2())
