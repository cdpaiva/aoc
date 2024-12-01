import sys


def distance(a, b):
    return abs(a - b)


def total_distance(col1, col2):
    return sum(distance(a, b) for a, b in zip(col1, col2))


def split_into_ints(lines):
    col1, col2 = list(zip(*lines))
    col1 = sorted(int(n) for n in col1)
    col2 = sorted(int(n) for n in col2)
    return col1, col2


def main(lines):
    col1, col2 = split_into_ints(lines)
    return total_distance(col1, col2)


if __name__ == "__main__":
    file_path = sys.argv[1]
    with open(file_path) as f:
        lines = [l.rstrip().split("   ") for l in f]

    print(main(lines))
