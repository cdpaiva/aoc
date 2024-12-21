import sys


def starting_pos(grid):
    for r, row in enumerate(grid):
        for c, square in enumerate(row):
            if square == "@":
                return (r, c)
    raise ValueError("Cannot find the robot's starting position.")


def main(lines):
    i = lines.index("")
    moves = list("".join(lines[i + 1 :]))
    grid = [list(l) for l in lines[:i]]

    r, c = starting_pos(grid)
    # replace robot's initial position
    directions = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}
    for move in moves:

        dr, dc = directions[move]
        front_block = grid[r + dr][c + dc]

        if front_block == "#":
            continue

        grid[r][c] = "."

        if front_block == ".":
            r += dr
            c += dc
        else:
            # push blocks in dr, dc direction
            front_blocks = []
            nr = r + dr
            nc = c + dc
            while grid[nr][nc] == "O":
                front_blocks.append((nr, nc))
                nr += dr
                nc += dc
            if grid[nr][nc] == "#":
                # cannot push if 'OOO#'
                grid[r][c] = "@"
                continue
            elif grid[nr][nc] == ".":
                # can shift all previous stones
                grid[nr][nc] = "O"
                grid[r + dr][c + dc] = "."
                r += dr
                c += dc
        grid[r][c] = "@"
    gps = 0
    for r, row in enumerate(grid):
        for c, square in enumerate(row):
            if square == "O":
                gps += r * 100 + c
    return gps


if __name__ == "__main__":
    file_path = sys.argv[1]

    with open(file_path, "r") as f:
        lines = [l.rstrip() for l in f]

    print(main(lines))
