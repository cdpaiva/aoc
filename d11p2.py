from collections import Counter
import sys


def main(stones, blinks=25):
    counter = Counter(stones)
    for _ in range(blinks):
        bfr_counter = Counter()
        for el, freq in counter.items():
            if el == "0":
                bfr_counter.update({"1": freq})
            elif len(el) % 2 == 0:
                mid = len(el) // 2
                left = el[:mid]
                right = str(int(el[mid:]))
                bfr_counter.update({left: freq})
                bfr_counter.update({right: freq})
            else:
                val = str(int(el) * 2024)
                bfr_counter.update({val: freq})
        counter = bfr_counter.copy()

    return sum(counter.values())


if __name__ == "__main__":
    file_path = sys.argv[1]

    with open(file_path, "r") as f:
        stones = f.readline().rstrip().split()

    print(main(stones, 75))
