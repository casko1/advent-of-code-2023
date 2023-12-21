from collections import defaultdict
from copy import deepcopy
from functools import reduce

lines = open("inputs/19.txt").read().split("\n\n")
rule_lines = lines[0].split("\n")
inputs = lines[1].split("\n")
rules_dict = defaultdict(lambda: defaultdict(list))

for line in rule_lines:
    label, *rules = line.split("{")
    rules = rules[0].replace("}", "")
    for rule in rules.split(","):
        if ":" in rule:
            spl = rule.split(":")
            rules_dict[label]["rules"].append((spl[0], spl[1]))  # (cond, target)
        else:
            rules_dict[label]["default"] = rule


def simulate():
    o = 0
    for inp in inputs:
        spl = "".join([x for x in inp if x not in "{}"]).split(",")
        x = int(spl[0].split("=")[1])
        m = int(spl[1].split("=")[1])
        a = int(spl[2].split("=")[1])
        s = int(spl[3].split("=")[1])
        reached_end = False
        current = "in"
        while not reached_end:
            current_rules = rules_dict[current]
            for r in current_rules["rules"]:
                if eval(r[0]):
                    current = r[1]
                    break
            else:
                current = current_rules["default"]

            if current in "A":
                reached_end = True
                o += x + m + a + s
            elif current in "R":
                reached_end = True

    return o


print(simulate())

range_map = {"x": 0, "m": 1, "a": 2, "s": 3}

out = []


def find_ranges(ranges, current):
    current_rules = rules_dict[current]

    if current == "A":
        return ranges

    if current == "R":
        return []

    for r in current_rules["rules"]:
        if "<" in r[0]:
            symbol, border = r[0].split("<")
            border = int(border)
            index = range_map[symbol]
            left_edge = border - 1
            right_edge = border
            left_range = deepcopy(ranges)
            right_range = deepcopy(ranges)
            left_range[index] = (left_range[index][0], left_edge)
            right_range[index] = (right_edge, right_range[index][1])
            out.append(find_ranges(left_range, r[1]))
            ranges = right_range

        if ">" in r[0]:
            symbol, border = r[0].split(">")
            index = range_map[symbol]
            border = int(border)
            left_edge = border
            right_edge = border + 1
            left_range = deepcopy(ranges)
            right_range = deepcopy(ranges)
            left_range[index] = (left_range[index][0], left_edge)
            right_range[index] = (right_edge, right_range[index][1])
            out.append(find_ranges(right_range, r[1]))
            ranges = left_range
    else:
        out.append(find_ranges(ranges, current_rules["default"]))

    return []


find_ranges([(1, 4000), (1, 4000), (1, 4000), (1, 4000)], "in")

s = 0
for solution in [r for r in out if len(r) > 0]:
    s += reduce(lambda x, y: x * y, [x[1] - x[0] + 1 for x in solution])

print(s)
