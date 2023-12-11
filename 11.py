import re
from itertools import combinations

lines = open("11.txt").read().split("\n")


def solve(step):
    offset_i = [i for i in range(len(lines)) if "#" not in lines[i]]
    transposed = list(zip(*lines))
    offset_j = [j for j in range(len(transposed)) if "#" not in transposed[j]]

    galaxies = []
    for i in range(len(lines)):
        for g in [(i, m.start(0)) for m in re.finditer(r"#", lines[i])]:
            n_i, n_j = g
            n_i += sum(1 for pos in offset_i if pos < g[0]) * step
            n_j += sum(1 for pos in offset_j if pos < g[1]) * step
            galaxies.append((n_i, n_j))

    return sum(abs(a[0] - b[0]) + abs(a[1] - b[1]) for a, b in set(combinations(galaxies, 2)))


print(solve(1))
print(solve(999999))
