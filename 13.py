patterns = open("inputs/13.txt").read().split("\n\n")


def mismatches(s1, s2):
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))


def reflection(pattern, allowed_mismatches, r=False):
    for i in range(len(pattern) - 1):
        if mismatches(pattern[i], pattern[i + 1]) <= allowed_mismatches:
            m = [mismatches(pattern[i - j], pattern[i + j + 1]) for j in range(min(i + 1, len(pattern) - i - 1))]
            if sum(m) == allowed_mismatches:
                return i + 1 if not r else len(pattern) - i - 1

    return 0


part1, part2 = 0, 0
for p in patterns:
    lines = p.split("\n")
    part1 += reflection(lines, 0) * 100
    part2 += reflection(lines, 1) * 100
    rotated = ["".join(x) for x in list(zip(*lines))[::-1]]
    part1 += reflection(rotated, 0, True)
    part2 += reflection(rotated, 1, True)

print(part1)
print(part2)
