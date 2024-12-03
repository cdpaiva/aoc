import re
import sys

pat = re.compile(r"mul\((\d+,\d+)\)")


def mul(line):
    acc = 0
    matches = re.finditer(pat, line)

    for match in matches:
        a, b = match.group(1).split(",")
        if len(a) > 3 or len(b) > 3:
            continue
        acc += int(a) * int(b)

    return acc


def main(lines):
    counter = 0
    for l in lines:
        counter += mul(l)
    return counter


if __name__ == "__main__":
    file_path = sys.argv[1]
    with open(file_path, "r") as f:
        lines = f.readlines()

    print(main(lines))
