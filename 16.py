from functools import reduce

m = [list(x) for x in open("inputs/16.txt").read().split("\n")]
directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]  # R = 0, L = 1, U = 2, D = 3
slash_map = {"/": {0: 2, 1: 3, 2: 0, 3: 1}, "\\": {0: 3, 1: 2, 3: 0, 2: 1}}


def energize(start, h, w):
    beam_queue = [start]
    visited_directions = set()
    visited = set()
    while len(beam_queue) > 0:
        b = beam_queue.pop(0)
        (n_i, n_j), d_i = b
        while 0 <= n_i < h and 0 <= n_j < w and ((n_i, n_j), d_i) not in visited_directions:
            visited_directions.add(((n_i, n_j), d_i))
            visited.add((n_i, n_j))
            c = m[n_i][n_j]

            if c == "|" and (d_i == 0 or d_i == 1):
                beam_queue.append(((n_i, n_j), 2))
                d_i = 3
            elif c == "-" and (d_i == 2 or d_i == 3):
                beam_queue.append(((n_i, n_j), 1))
                d_i = 0
            elif c in "/\\":
                d_i = slash_map[m[n_i][n_j]][d_i]

            direction = directions[d_i]
            n_i, n_j = n_i + direction[0], n_j + direction[1]

    return len(visited)


print(energize(((0, 0), 0), len(m), len(m[0])))

max_energized = 0
for n in range(len(m)):
    coordinates = [((n, 0), 0), ((n, len(m) - 1), 1), ((0, n), 3), ((len(m) - 1, n), 2)]
    max_energized = reduce(lambda acc, coord: max(acc, energize(coord, len(m), len(m[0]))), coordinates, max_energized)

print(max_energized)
