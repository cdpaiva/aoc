import sys


def main(schematics):
    keys = []
    locks = []

    filled_row = "#" * len(schematics[0][0])
    for sc in schematics:
        heights = [0 for _ in range(len(sc[0]))]
        if sc[0] == filled_row:
            for row in sc[1:]:
                for c, square in enumerate(row):
                    if square == "#":
                        heights[c] += 1
        elif sc[-1] == filled_row:
            for row in sc[:-1]:
                for c, square in enumerate(row):
                    if square == "#":
                        heights[c] += 1
        keys.append(heights)

    count = 0
    for lock in locks:
        for key in keys:
            if all(lh + kh <= 5 for (lh, kh) in zip(lock, key)):
                count += 1

    return count


if __name__ == "__main__":
    file_path = sys.argv[1]

    with open(file_path, "r") as f:
        schematics = [l.rstrip().split("\n") for l in f.read().split("\n\n")]

    print(main(schematics))
