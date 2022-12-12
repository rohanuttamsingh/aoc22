from os.path import join

def parse_input(debug=False):
    filename = f"input/{'test' if debug else '7'}.txt"
    with open(filename, 'r') as f:
        raw = f.read().split('$')[1:]
    seq_split = [seq.split('\n') for seq in raw]
    for seq in seq_split:
        seq[0] = seq[0][1:]
    return [seq[:-1] for seq in seq_split]

def parse_ls_lines(lines):
    dir_size = 0
    for line in lines:
        if not line.startswith('dir'):
            size, _ = line.split(' ')
            dir_size += int(size)
    return dir_size

def get_all_dirs(curr_path):
    dirs = []
    for i in range(1, len(curr_path) + 1):
        dir = ''
        for j in range(i):
            dir = join(dir, curr_path[j])
        dirs.append(dir)
    return dirs

def get_dir_sizes(debug=False):
    seqs = parse_input(debug=debug)
    dir_sizes = {}
    processed_dirs = set()
    curr_path = []
    for seq in seqs:
        cmd = seq[0]
        if cmd.startswith('cd'):
            new_dir = cmd[3:]
            if new_dir == '..':
                curr_path = curr_path[:-1]
            else:
                curr_path.append(new_dir)
        else:
            dirs_to_update = get_all_dirs(curr_path)
            if dirs_to_update[-1] not in processed_dirs:
                dir_size = parse_ls_lines(seq[1:])
                for dir in dirs_to_update:
                    if dir not in dir_sizes:
                        dir_sizes[dir] = 0
                    dir_sizes[dir] += dir_size
                processed_dirs.add(dirs_to_update[-1])
    return dir_sizes

def part1():
    dir_sizes = get_dir_sizes()
    return sum(filter(lambda x: x <= 100000, dir_sizes.values()))

def part2():
    dir_sizes = get_dir_sizes()
    free_space = 70000000 - dir_sizes['/']
    needed_space = 30000000 - free_space
    return min(filter(lambda x: x >= needed_space, dir_sizes.values()))

print(part1())
print(part2())
