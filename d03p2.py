import re
import sys

pat = re.compile(r"mul\((\d+,\d+)\)|(do\(\))|(don't\(\))")


def mul(line):
    acc = 0
    matches = re.finditer(pat, line)
    is_enabled = True

    for match in matches:
        if match.group(0) == "do()":
            is_enabled = True
        elif match.group(0) == "don't()":
            is_enabled = False
        else:
            a, b = match.group(1).split(",")
            if len(a) > 3 or len(b) > 3:
                continue
            if is_enabled:
                acc += int(a) * int(b)

    return acc


def main(lines):
    return mul("".join(lines))


if __name__ == "__main__":
    file_path = sys.argv[1]
    with open(file_path, "r") as f:
        lines = f.readlines()

    print(main(lines))
