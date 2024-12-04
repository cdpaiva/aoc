import sys


def search(lines, r, c, target):
    counter = 0
    rows = len(lines)
    cols = len(lines[0])
    dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for dr, dc in dirs:
        word = ""
        rr = r
        cc = c
        for _ in range(3):
            rr += dr
            cc += dc
            if rr < 0 or rr >= rows or cc < 0 or cc >= cols:
                break
            word += lines[rr][cc]
        if word == target:
            counter += 1
    return counter


def find_words(lines, word):
    count = 0
    for r, row in enumerate(lines):
        for c, _ in enumerate(row):
            if lines[r][c] == word[0]:
                count += search(lines, r, c, word[1:])
    return count


def main(lines):
    return find_words(lines, "XMAS")


if __name__ == "__main__":
    file_path = sys.argv[1]
    with open(file_path, "r") as f:
        lines = [list(l.rstrip()) for l in f.readlines()]

    print(main(lines))
