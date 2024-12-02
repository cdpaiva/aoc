import sys


def check_subsequence(line, i, increasing):
    line = line.copy()
    line.pop(i)
    deltas = [b - a for a, b in zip(line[:-1], line[1:])]
    if increasing:
        return all(d > 0 and d < 4 for d in deltas)
    else:
        return all(d < 0 and d > -4 for d in deltas)


def is_safe(line):
    deltas = [b - a for a, b in zip(line[:-1], line[1:])]
    increasing = sum(1 for d in deltas if d > 0) > (len(deltas) // 2)
    for i, d in enumerate(deltas):
        if increasing:
            if d < 1 or d > 3:
                return check_subsequence(line, i, increasing) or check_subsequence(
                    line, i + 1, increasing
                )
        else:
            if d > -1 or d < -3:
                return check_subsequence(line, i, increasing) or check_subsequence(
                    line, i + 1, increasing
                )
    return True


def main(lines):
    return sum(1 for l in lines if is_safe(l))


if __name__ == "__main__":
    file_path = sys.argv[1]
    with open(file_path, "r") as f:
        lines = f.readlines()

    lines = [[int(n) for n in l.split()] for l in lines]

    print(main(lines))
