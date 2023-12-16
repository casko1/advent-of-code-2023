from collections import defaultdict, OrderedDict
from functools import reduce
import re


def hash_string(s):
    return reduce(lambda acc, x: ((acc + x) * 17) % 256, list(map(ord, s)), 0)


instructions = open("inputs/15.txt").readline().split(",")

boxes = defaultdict(OrderedDict)
pattern = re.compile(r"[a-zA-Z]+|\d+")
for inst in instructions:
    match re.findall(pattern, inst):
        case [label, f]: boxes[hash_string(label)].update({label: int(f)})
        case [label]: boxes[hash_string(label)].pop(label, None)

part2 = 0
for i, box in boxes.items():
    for j, (_, f) in enumerate(box.items()):
        part2 += (i + 1) * (j + 1) * f

print(sum(map(hash_string, instructions)))
print(part2)
