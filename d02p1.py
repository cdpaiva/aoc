import sys


def is_safe(l):
    increasing = l[0] < l[1]
    for a, b in zip(l[:-1], l[1:]):
        if increasing:
            if b - a > 3 or b - a < 1:
                return False
        else:
            if a - b > 3 or a - b < 1:
                return False
    return True


def main(lines):
    return sum([1 for l in lines if is_safe(l)])


if __name__ == "__main__":
    file_path = sys.argv[1]
    with open(file_path, "r") as f:
        lines = f.readlines()

    lines = [[int(n) for n in l.split()] for l in lines]
    print(main(lines))
