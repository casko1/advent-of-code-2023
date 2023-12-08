import math
import re


lines = open("8.txt").read().split("\n\n")

instructions = [0 if x == "L" else 1 for x in lines[0]]
nodes_list = re.findall(r"\w+", lines[1])
a_nodes = []
nodes = {}

for i in range(0, len(nodes_list), 3):
    nodes[nodes_list[i]] = (nodes_list[i+1], nodes_list[i+2])
    if nodes_list[i][2] == "A":
        a_nodes.append(nodes_list[i])

current = "AAA"
part1 = 0
while current != "ZZZ":
    idx = instructions[part1 % len(instructions)]
    current = nodes[current][idx]
    part1 += 1

print(part1)

cycle_lengths = []
for node in a_nodes:
    cycle_length = 0
    current = node
    visited = {}
    while True:
        idx = instructions[cycle_length % len(instructions)]

        if f"{current}_{idx}" in visited and current[2] == "Z":
            break

        visited[f"{current}_{idx}"] = cycle_length

        current = nodes[current][idx]
        cycle_length += 1

    cycle_lengths.append(visited[f"{current}_{idx}"])

print(math.lcm(*cycle_lengths))
