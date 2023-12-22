m = [list(line) for line in open("inputs/21.txt").read().split("\n")]

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

size = len(m)
start = (0, 0)

for i in range(size):
    for j in range(size):
        if m[i][j] == "S":
            start = (i, j)


def find_reachable(steps):
    reachable = {start}
    for i in range(steps):
        new_reachable = set()
        for plot_y, plot_x in reachable:
            for d_y, d_x in directions:
                n_y, n_x = plot_y + d_y, plot_x + d_x
                if m[n_y % size][n_x % size] != "#":
                    new_reachable.add((n_y, n_x))

        reachable = new_reachable

    return len(reachable)


def fit_polynomial():
    # grid sizes: 1...5...13...25 etc. -> we can get the "n-th" grid size via some quadratic function ax^2 + bx + c
    # with knowing the fact that 26501365 - 65 mod 131 is 0 (is divisible by) and the fact the area increases
    # following a quadratic function we can calculate f(65), f(65 + 1 * 131), f(65 + 2 * 131), which is 3 points
    # of the curve we need to figure out a, b and c. In more general terms:
    # f(0) = c
    # f(1) = a + b + c -> b = f(1) - a - c
    # f(2) = 4a + 2b + c -> 4a + 2f(1) - 2a - 2c + c => a = f(2)/2 - f(1) + c/2
    # a = f(2)/2 - f(1) - f(0)/2
    # b = f(1) - a - f(0)
    # c = f(0)
    f_0 = find_reachable(65)
    f_1 = find_reachable(65 + 131)
    f_2 = find_reachable(65 + 131*2)

    c = f_0
    a = f_2 / 2 - f_1 + c / 2
    b = f_1 - a - c
    x = (26501365 - 65) / 131  # looking for n-th step

    return a * x**2 + b * x + c


print(find_reachable(64))
print(f"{fit_polynomial():.0f}")
