import math
import re

lines = open("inputs/8.txt").read().split("\n\n")
instructions = [0 if x == "L" else 1 for x in lines[0]]
nodes_list = re.findall(r"\w+", lines[1])
a_nodes = []
nodes = {}

for i in range(0, len(nodes_list), 3):
    nodes[nodes_list[i]] = (nodes_list[i + 1], nodes_list[i + 2])
    if nodes_list[i][2] == "A":
        a_nodes.append(nodes_list[i])


def solve(start_nodes, condition):
    out = []
    for node in start_nodes:
        step = 0
        current = node
        while condition(current):
            idx = instructions[step % len(instructions)]
            current = nodes[current][idx]
            step += 1
        out.append(step)

    return out


print(*solve(["AAA"], lambda x: x != "ZZZ"))
print(math.lcm(*solve(a_nodes, lambda x: x[2] != "Z")))
