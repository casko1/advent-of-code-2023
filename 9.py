lines = open("9.txt").read().split("\n")
histories = [[int(x) for x in line.split()] for line in lines]


def solve(current):
    diffs = [current]
    while sum(current) != 0:
        current = [current[i + 1] - current[i] for i in range(len(current) - 1)]
        diffs.insert(0, current)

    for i in range(len(diffs) - 1):
        diffs[i + 1].append(diffs[i + 1][-1] + diffs[i][-1])
        diffs[i + 1].insert(0, diffs[i + 1][0] - diffs[i][0])

    return diffs[-1][-1], diffs[-1][0]


solutions = list(map(sum, zip(*[solve(x) for x in histories])))
print(solutions[0])
print(solutions[1])
