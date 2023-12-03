import re
from collections import defaultdict

lines = open("3.txt").read().split("\n")
lines.append("." * len(lines[0]))
lines.insert(0, lines[-1])

numbers = [[(m.start(0), m.end(0)) for m in re.finditer(r"(\d+)", line)] for line in lines]
special = [[(m.start(0), i) for m in re.finditer(r"([^a-zA-Z0-9.])", line)] for i, line in enumerate(lines)]

symbol_dict = defaultdict(list)

part1 = 0

for i, line in enumerate(lines):
    nums = numbers[i]
    for n_start, n_end in nums:
        special_c = [*[x for x in special[i - 1]], *[x for x in special[i + 1]], *[x for x in special[i]]]
        for s, y in special_c:
            if abs(n_start - s) <= 1 or abs(n_end - 1 - s) <= 1:
                value = int(lines[i][n_start:n_end])
                part1 += value
                if lines[y][s] == "*":
                    symbol_dict[f"{y},{s}"].append(value)

print(part1)
print(sum(x[0] * x[1] for x in symbol_dict.values() if len(x) == 2))
