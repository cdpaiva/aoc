import sys
from collections import Counter


rows = 101
cols = 103


def freqs_by_quadrant(pos):
    mid_row = rows // 2
    mid_col = cols // 2
    quadrants = [0, 0, 0, 0]
    for (
        (r, c),
        freq,
    ) in pos.items():
        if r < mid_row and c < mid_col:
            quadrants[0] += freq
        if r < mid_row and c > mid_col:
            quadrants[1] += freq
        if r > mid_row and c < mid_col:
            quadrants[2] += freq
        if r > mid_row and c > mid_col:
            quadrants[3] += freq
    return quadrants


def walk(robot, num_steps):
    r, c, dr, dc = robot
    for _ in range(num_steps):
        r += dr
        c += dc
        if r < 0:
            r += rows
        if r >= rows:
            r -= rows
        if c < 0:
            c += cols
        if c >= cols:
            c -= cols
    return r, c


def main(robots):
    final_pos = []
    for robot in robots:
        pos = walk(robot, 100)
        final_pos.append(pos)
    pos_counter = Counter(final_pos)
    a, b, c, d = freqs_by_quadrant(pos_counter)
    return a * b * c * d


if __name__ == "__main__":
    file_path = sys.argv[1]

    with open(file_path, "r") as f:
        lines = [l.rstrip() for l in f]

    robots = []
    for l in lines:
        pos, v = l.split()
        r, c = pos[2:].split(",")
        dr, dc = v[2:].split(",")
        robots.append((int(r), int(c), int(dr), int(dc)))

    print(main(robots))
