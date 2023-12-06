import re
from collections import defaultdict

lines = open("5.txt").read().split("\n\n")
seeds = list(map(int, re.findall(r"\d+", lines[0])))
maps = defaultdict(list)
VERY_LARGE_NUMBER = 9999999999999999

for k, m in enumerate(lines[1::]):
    mappings = m.split("\n")[1::]

    for mapping in mappings:
        spl = mapping.split()
        maps[k].append((int(spl[1]), int(spl[0]), int(spl[2])))


def part1():
    minimum = VERY_LARGE_NUMBER
    for seed in seeds:
        current_val = int(seed)

        for i in range(7):
            current_map = maps[i]

            for entry in current_map:
                if entry[0] <= current_val <= entry[0] + entry[2]:
                    current_val = entry[1] + (current_val - entry[0])
                    break

        if current_val < minimum:
            minimum = current_val

    return minimum


def part2():
    seed_ranges = [(seeds[i], seeds[i] + seeds[i + 1]) for i in range(0, len(seeds), 2)]
    for i in range(VERY_LARGE_NUMBER):
        current_val = i

        for j in range(7):
            current_map = maps[6 - j]

            for entry in current_map:
                if entry[1] <= current_val < entry[1] + entry[2]:
                    current_val = entry[0] + (current_val - entry[1])
                    break

        for s in seed_ranges:
            if s[0] <= current_val <= s[1]:
                return i


print(part1())
print(part2())
