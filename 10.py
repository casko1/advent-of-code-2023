import re
from collections import defaultdict

lines = open("10.txt").read().split("\n")
start = []

directions = {"|": [(1, 0), (-1, 0)], "-": [(0, 1), (0, -1)], "L": [(-1, 0), (0, 1)], "J": [(-1, 0), (0, -1)],
              "7": [(1, 0), (0, -1)], "F": [(1, 0), (0, 1)], ".": [], "S": [(1, 0), (-1, 0), (0, 1), (0, -1)]}

for i in range(len(lines)):
    lines[i] = f".{lines[i]}."
    start.extend((i + 1, m.start(0)) for m in re.finditer(r"S", lines[i]))

lines.append("." * (len(lines[0])))
lines.insert(0, lines[-1])

q = [("S", start[0], 0)]
visited = defaultdict(lambda: 999999999999999)
visited[start[0]] = 0

while len(q) != 0:
    symbol, (i, j), distance = q.pop(0)
    for d in directions[symbol]:
        n_i, n_j = i + d[0], j + d[1]
        n_symbol = lines[n_i][n_j]
        if (-d[0], -d[1]) in directions[n_symbol] and symbol != "." and distance + 1 < visited[(n_i, n_j)]:
            q.append((n_symbol, (n_i, n_j), distance + 1))
            visited[(n_i, n_j)] = distance + 1

enclosed = 0
for i in range(1, len(lines) - 1):
    intersections = 0
    previous = []
    for j in range(1, len(lines[0]) - 1):
        current = (i, j)
        symbol = lines[i][j]
        if current in visited:
            if symbol == "-":
                continue
            if symbol == "|" or previous == "L" and symbol == "7" or previous == "F" and symbol == "J":
                intersections += 1
            elif symbol == "L" or symbol == "F":
                previous = symbol
        elif intersections % 2 == 1:
            enclosed += 1

print(max(visited.values()))
print(enclosed)
