import math
import re
from functools import reduce

lines = [re.findall(r"\d+", line) for line in open("6.txt").read().split("\n")]
nums = [(int(x), int(y)) for x, y in zip(lines[0], lines[1])]


def quadratic(b, c):
    d = b ** 2 - 4 * c
    sqrt_val = math.sqrt(abs(d))
    r_d = (b + sqrt_val) / 2
    r_l = (b - sqrt_val) / 2
    return math.ceil(r_d) - math.floor(r_l) - 1


print(reduce(lambda x, y: x * y, [quadratic(b, c) for b, c in nums]))
print(quadratic(int("".join(lines[0])), int("".join(lines[1]))))
