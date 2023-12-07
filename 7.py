from collections import Counter

lines = open("7.txt").read().split("\n")
replacements = {"A": "Z", "K": "Y", "Q": "X", "J": "W", "T": "V"}


def part1():
    grouped_hands = []

    for line in lines:
        hand, bet = line.split(" ")
        hand = "".join([replacements.get(i, i) for i in hand])

        c = Counter(hand)
        key = "".join(str(x) for x in sorted(c.values(), reverse=True))
        grouped_hands.append((key, hand, int(bet)))

    grouped_hands = sorted(grouped_hands, key=lambda x: (x[0], x[1]))
    return sum([grouped_hands[i][2] * (i + 1) for i in range(len(grouped_hands))])


def part2():
    grouped_hands = []
    for line in lines:
        hand, bet = line.split(" ")
        replacements["J"] = "0"
        hand = "".join([replacements.get(i, i) for i in hand])

        c_d = Counter(hand)
        c = sorted(c_d.items(), key=lambda x: (x[1], x[0]), reverse=True)
        joker = ("0", c_d.get("0", -1))

        if joker[1] != -1 and len(c) > 1:
            p = 1 if c.index(joker) == 0 else 0
            c[p] = (c[p][0], c[p][1] + joker[1])
            c.remove(joker)

        key = "".join(str(x[1]) for x in c)
        grouped_hands.append((key, hand, int(bet)))

    grouped_hands = sorted(grouped_hands, key=lambda x: (x[0], x[1]))
    return sum([grouped_hands[i][2] * (i + 1) for i in range(len(grouped_hands))])


print(part1())
print(part2())
