lines = open("14.txt").read().split("\n")
mat = [[x for x in y] for y in lines]
height = len(mat)

rotate_coordinates = [
    lambda x, y: (x, y),
    lambda x, y: (height - 1 - y, x),
    lambda x, y: (height - 1 - x, height - 1 - y),
    lambda x, y: (y, height - 1 - x)
]


def step(m, r):
    coords = []
    for j in range(height):
        for ind in range(height):
            if m[ind][j] == "O":
                k = ind
                while k > 0 and m[k - 1][j] not in "#O":
                    m[k - 1][j], m[k][j] = m[k][j], m[k - 1][j]
                    k -= 1
        else:
            for p in range(len(m)):
                if m[p][j] == "O":
                    coords.append(rotate_coordinates[r](p, j))

    return tuple(coords)


known = {}
part1, part2 = None, None
for i in range(4 * 1_000_000_000):
    c = step(mat, i % 4)
    if i == 1:
        part1 = c
    if c in known:
        k_i = known[c]
        target = (4 * 1_000_000_000 - 1 - k_i) % (i - k_i) + k_i
        for key, value in known.items():
            if value == target:
                part2 = key
                break
        break

    known[c] = i
    mat = [list(x) for x in zip(*mat[::-1])]

print(sum(height - x[0] for x in part1))
print(sum(height - x[0] for x in part2))
