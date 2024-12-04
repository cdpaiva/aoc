import sys


def is_MS(lines, r, c, diag):
    rows = len(lines)
    cols = len(lines[0])
    word = ""
    for dr, dc in diag:
        rr = r + dr
        cc = c + dc
        if rr < 0 or rr >= rows or cc < 0 or cc >= cols:
            break
        word += lines[rr][cc]
    return word == "MS" or word == "SM"


def find_MAS_cross(lines):
    diags = ((-1, -1), (1, 1)), ((-1, 1), (1, -1))
    count = 0
    for r, row in enumerate(lines):
        for c, _ in enumerate(row):
            if lines[r][c] == "A":
                if is_MS(lines, r, c, diags[0]) and is_MS(lines, r, c, diags[1]):
                    count += 1
    return count


def main(lines):
    return find_MAS_cross(lines)


if __name__ == "__main__":
    file_path = sys.argv[1]
    with open(file_path, "r") as f:
        lines = [list(l.rstrip()) for l in f.readlines()]

    print(main(lines))
