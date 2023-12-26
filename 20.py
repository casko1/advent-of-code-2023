import math
import re

lines = open("inputs/20.txt").read().split("\n")

modules = {}

for line in lines:
    name, *neighbours = re.findall(r"([%&]?\w+)", line)
    match name[0]:
        case "b": modules[name] = [neighbours, None, "b"]
        case "%": modules[name[1:]] = [neighbours, 0, name[0]]
        case "&": modules[name[1:]] = [neighbours, {}, name[0]]

for k, v in modules.items():
    for n in v[0]:
        if n in modules and modules[n][2] == "&":
            modules[n][1][k] = 0

# with manual inspection there is only one conjunction node leading to rx and to this node there are 4 additional
# conjunction nodes. Find lcm of these nodes. I assume this holds for every AoC input
last_node = [x for x in modules.keys() if "rx" in modules[x][0]][0]
last_to_last_nodes = [x for x in modules.keys() if last_node in modules[x][0]]
cycle_lengths = [0, 0, 0, 0]


def simulate(index):
    q = [("broadcaster", 0)]
    out = [1, 0]

    while len(q) != 0:
        if index > 0:
            for p, node in enumerate(last_to_last_nodes):
                if sum(modules[node][1].values()) != len(modules[node][1].values()) and cycle_lengths[p] == 0:
                    cycle_lengths[p] = index + 1

        key, signal, *sender = q.pop(0)

        if key not in modules:
            continue

        neighbor_nodes, state, op = modules[key]

        if state is None:
            q.extend([(neighbor, signal) for neighbor in neighbor_nodes])
            out[0] += len(neighbor_nodes)

        if op == "%" and signal == 0:
            new_state = (state + 1) % 2
            out[new_state] += len(neighbor_nodes)
            modules[key][1] = new_state
            for node in [x for x in neighbor_nodes if x in modules]:
                q.append((node, new_state, key))

        if op == "&":
            s_key = sender[0]
            modules[key][1][s_key] = signal
            out_signal = 0 if all(x == 1 for x in state.values()) else 1
            out[out_signal] += len(neighbor_nodes)
            for node in [x for x in neighbor_nodes if x in modules]:
                q.append((node, out_signal, key))

    return out


low_acc, high_acc = 0, 0
part2 = 0
for i in range(1000000000):
    if all(x != 0 for x in cycle_lengths):
        part2 = math.lcm(*cycle_lengths)
        break

    low, high = simulate(i)
    if i < 1000:
        low_acc += low
        high_acc += high

print(low_acc * high_acc)
print(part2)
