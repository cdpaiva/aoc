import sys


def num_pushes(xa, ya, xb, yb, x, y):
    na = (y * xb - x * yb) / (ya * xb - xa * yb)
    nb = (x - na * xa) / xb
    return na, nb


def parse_line(line, sep):
    _, vals = line.split(": ")
    x, y = vals.split(", ")
    x_inc = int(x.split(sep)[1])
    y_inc = int(y.split(sep)[1])
    return x_inc, y_inc


if __name__ == "__main__":
    file_path = sys.argv[1]
    with open(file_path, "r") as f:
        lines = [l.rstrip() for l in f]

    cost = 0
    for i in range(0, len(lines), 4):
        line_a, line_b, prize, _ = lines[i : i + 4]
        xa, ya = parse_line(line_a, sep="+")
        xb, yb = parse_line(line_b, sep="+")
        x, y = parse_line(prize, sep="=")
        print(xa, ya)
        print(xb, yb)
        print(x, y)
        na, nb = num_pushes(xa, ya, xb, yb, x, y)
        if int(na) == na and int(nb) == nb:
            print("Recheable!")
            cost += 3 * na + nb
        print(na, nb)
        print()

    print(cost)
