import sys


def combinable(comb, towels):
    stack = []
    i = 0
    stack.append(i)

    while stack:
        curr = stack.pop()
        if curr >= len(comb):
            return True
        for i in range(len(comb) - curr + 1):
            if comb[curr : curr + i] in towels:
                stack.append(curr + i)
    return False


def main(towels, combinations):
    return sum(1 for c in combinations if combinable(c, towels))


if __name__ == "__main__":
    file_path = sys.argv[1]

    with open(file_path, "r") as f:
        lines = [l.rstrip() for l in f]

    towels = {t for t in lines[0].split(", ")}
    combinations = lines[2:]

    print(main(towels, combinations))
