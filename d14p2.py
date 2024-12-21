import sys
from collections import Counter
import matplotlib.pyplot as plt
import matplotlib.animation as animation


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
    single = True
    animate = False
    if single:
        i = 80 * 101 + 99
        final_pos = [walk(robot, i) for robot in robots]

        grid = [[0] * cols for _ in range(rows)]
        for r, c in final_pos:
            grid[r][c] += 1

        fig, ax = plt.subplots()
        im = ax.imshow(grid)
        frame_num = ax.text(0, 0, "0")

        def updateGrid(i):
            frame_num.set_text(str(i))
            final_pos = [walk(robot, i * 101 + 99) for robot in robots]
            grid = [[0] * cols for _ in range(rows)]
            for r, c in final_pos:
                grid[r][c] += 1
            im.set_array(grid)

        if animate:
            ani = animation.FuncAnimation(fig, updateGrid, interval=500)

        plt.show()
        return

    fig, ax = plt.subplots()
    ff = []
    for i in range(100, 500):
        final_pos = [walk(robot, i) for robot in robots]
        counter = Counter(final_pos)
        a, b, c, d = freqs_by_quadrant(counter)
        ff.append(a)
    ax.plot(ff)
    plt.show()


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
