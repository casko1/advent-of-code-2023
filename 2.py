import re
from collections import defaultdict


def parse(text):
    out = defaultdict(int)
    data = list(map(lambda w: re.sub(r"\W+", "", w), text.split()))
    for value, key in zip(data[0::2], data[1::2]):
        out[key] = max(out[key], int(value))

    return [out["red"], out["green"], out["blue"]]


lines = open("2.txt").readlines()

part1 = 0
part2 = 0

for line in lines:
    spl = line.split(":")
    game_id = int(spl[0].split()[1])
    r, g, b = parse(spl[1])
    if r <= 12 and g <= 13 and b <= 14:
        part1 += game_id
    part2 += r * g * b

print(part1)
print(part2)
