import sys


def main(blocks):
    checksum = 0
    total_space = sum(n for n in blocks[::2])

    compressed = []

    right = -1
    for i, n in enumerate(blocks):
        if len(compressed) >= total_space:
            break
        if i % 2 == 0:
            id = i // 2
            for _ in range(n):
                compressed.append(id)
        else:
            for _ in range(n):
                if blocks[right] == 0:
                    right -= 2
                id = (len(blocks) + right) // 2
                compressed.append(id)
                blocks[right] -= 1

    for i, n in enumerate(compressed[:total_space]):
        checksum += i * n

    return checksum


if __name__ == "__main__":
    file_path = sys.argv[1]
    with open(file_path, "r") as f:
        blocks = [int(n) for n in list(f.read().rstrip())]

    print(main(blocks))
