from collections import Counter
import sys

from d01p1 import split_into_ints


def similarity(n, occurs):
    return n * occurs


def main(lines):
    col1, col2 = split_into_ints(lines)
    freqs = Counter(col2)

    return sum(similarity(n, freqs.get(n, 0)) for n in col1)


if __name__ == "__main__":
    file_path = sys.argv[1]
    with open(file_path) as f:
        lines = [l.rstrip().split("   ") for l in f]

    print(main(lines))
