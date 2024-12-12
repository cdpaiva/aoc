import sys


def main(stones, blinks=25):
    for _ in range(blinks):
        next_blink = []
        for s in stones:
            if s == 0:
                next_blink.append(1)
            elif len(str(s)) % 2 == 0:
                ss = str(s)
                mid = len(ss) // 2
                next_blink.append(int(str(ss[:mid])))
                next_blink.append(int(str(ss[mid:])))
            else:
                next_blink.append(s * 2024)
        stones = next_blink

    return len(stones)


if __name__ == "__main__":
    file_path = sys.argv[1]

    with open(file_path, "r") as f:
        stones = [int(n) for n in f.readline().split()]

    print(main(stones))
