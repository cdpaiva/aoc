import sys


def rotate(dr, dc):
    if dr == -1 and dc == 0:
        return (0, 1)
    if dr == 0 and dc == 1:
        return (1, 0)
    if dr == 1 and dc == 0:
        return (0, -1)
    if dr == 0 and dc == -1:
        return (-1, 0)
    raise ValueError(f"Unexpected direction: {dir}")


def peek(r, c, dr, dc, grid):
    rows = len(grid)
    cols = len(grid[0])
    r += dr
    c += dc
    if r < 0 or r >= rows or c < 0 or c >= cols:
        return "end"
    return grid[r][c]


def walk(r, c, dr, dc, grid, counter=0):
    next_square = peek(r, c, dr, dc, grid)

    while next_square != "end":
        if next_square == "#":
            dr, dc = rotate(dr, dc)
        else:
            r += dr
            c += dc
            # mark visited squares
            grid[r][c] = "X"
            counter += 1
        next_square = peek(r, c, dr, dc, grid)

    return counter


def get_starting_pos(grid):
    for r, row in enumerate(grid):
        for c, _ in enumerate(row):
            if grid[r][c] == "^":
                return (r, c)
    raise ValueError("Could not find initial position")


def main(grid):
    r, c = get_starting_pos(grid)
    # initial direction is North:
    dr = -1
    dc = 0
    counter = walk(r, c, dr, dc, grid)
    counter = 0
    for row in grid:
        for el in row:
            if el == "X":
                counter += 1
    return counter


if __name__ == "__main__":
    file_path = sys.argv[1]

    with open(file_path, "r") as f:
        grid = [list(l.rstrip()) for l in f]

    print(main(grid))
