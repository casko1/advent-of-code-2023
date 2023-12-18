import heapq

m = [[int(x) for x in list(line)] for line in open("inputs/17.txt").read().split("\n")]
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # R = 0, D = 1, L = 2, U = 3
nonsense = {0: 2, 2: 0, 1: 3, 3: 1}


def find_heat(min_steps, max_steps):
    visited = set()
    q = [(0, (0, 0), (0, 1)), (0, (0, 0), (1, 1))]  # (heat, (i, j), (previous_direction, count))
    while len(q) != 0:
        heat, position, (previous_direction, previous_count) = heapq.heappop(q)
        if (position, (previous_direction, previous_count)) in visited:
            continue
        else:
            visited.add((position, (previous_direction, previous_count)))

        i, j = position
        d_i, d_j = directions[previous_direction]
        n_i, n_j = i + d_i, j + d_j

        if not (0 <= n_i < len(m) and 0 <= n_j < len(m)):
            continue

        new_heat = heat + m[n_i][n_j]
        if min_steps <= previous_count <= max_steps and n_i == len(m) - 1 and n_j == len(m[0]) - 1:
            return new_heat

        for direction in range(4):
            if previous_direction == nonsense[direction]:
                continue

            new_direction_count = previous_count + 1 if previous_direction == direction else 1
            if (direction != previous_direction and previous_count < min_steps) or new_direction_count > max_steps:
                continue

            heapq.heappush(q, (new_heat, (n_i, n_j), (direction, new_direction_count)))


print(find_heat(1, 3))
print(find_heat(4, 10))
