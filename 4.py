from collections import defaultdict

lines = open("4.txt").read().split("\n")
number_of_scratchcards = defaultdict(int)

part1 = 0

for i, line in enumerate(lines):
    numbers = line.split(":")[-1].split("|")
    m = set([int(x) for x in numbers[0].split()]) & set([int(x) for x in numbers[1].split()])

    for k in range(len(m)):
        number_of_scratchcards[i+k+1] += (number_of_scratchcards[i] + 1)

    if len(m) > 0:
        part1 += 2**(len(m) - 1)

print(part1)
print(len(lines) + sum(number_of_scratchcards.values()))
