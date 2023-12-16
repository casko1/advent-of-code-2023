import re

lines = open("inputs/1.txt").readlines()
part1 = 0
part2 = 0
for line in lines:
    x = re.findall(r"(\d)", line)
    if len(x) > 0:
        part1 += int(x[0] + x[-1])

word_to_num = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

for line in lines:
    x = list(map(lambda y: word_to_num.get(y, y), re.findall(r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))", line)))
    part2 += int(x[0] + x[-1])

print(part1)
print(part2)
