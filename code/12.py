def valid_neighbor(height, neighbor_height, reverse):
    if height == 'S':
        height = 'a'
    elif height == 'E':
        height = 'z'
    if neighbor_height == 'S':
        neighbor_height = 'a'
    elif neighbor_height == 'E':
        neighbor_height = 'z'
    if reverse:
        return ord(height) - ord(neighbor_height) <= 1
    return ord(neighbor_height) - ord(height) <= 1

def process_input(debug, reverse):
    with open(f"input/{'test' if debug else '12'}.txt", 'r') as f:
        raw = f.read().strip().split('\n')
    heights = [list(s) for s in raw]
    graph = {}
    as_ = []
    for row in range(len(heights)):
        for col in range(len(heights[0])):
            if heights[row][col] == 'S':
                S = (row, col)
                as_.append((row, col))
            elif heights[row][col] == 'a':
                as_.append((row, col))
            elif heights[row][col] == 'E':
                E = (row, col)
            neighbors = []
            dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for row_dir, col_dir in dirs:
                new_row, new_col = row + row_dir, col + col_dir
                if 0 <= new_row < len(heights) and 0 <= new_col < len(heights[0]):
                    if valid_neighbor(heights[row][col], heights[new_row][new_col], reverse):
                        neighbors.append((new_row, new_col))
            graph[(row, col)] = neighbors
    return graph, S, E, as_

def dijkstra(graph, S):
    d = {coord: float('inf') if coord != S else 0 for coord in graph}
    explored = {coord: False for coord in graph}
    while False in explored.values():
        u, dist = min(filter(lambda x: not explored[x[0]], d.items()), key=lambda x: x[1])
        for v in graph[u]:
            if dist + 1 < d[v]:
                d[v] = dist + 1
        explored[u] = True
    return d

def part1(debug=False):
    graph, S, E, _ = process_input(debug, False)
    d = dijkstra(graph, S)
    return d[E]

def part2(debug=False):
    graph, _, E, as_ = process_input(debug, True)
    d = dijkstra(graph, E)
    return min([d[a] for a in as_])

print(part1())
print(part2())
