import sys


def score(r, c, grid):
    rows = len(grid)
    cols = len(grid[0])
    neighbors = ((-1, 0), (1, 0), (0, 1), (0, -1))
    stack = [(r, c)]

    trail_end = []
    while stack:
        r, c = stack.pop()
        for dr, dc in neighbors:
            nr = r + dr
            nc = c + dc
            if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                continue
            if grid[nr][nc] == 9 and grid[r][c] == 8:
                trail_end.append((nr, nc))
                continue
            if grid[nr][nc] == grid[r][c] + 1:
                stack.append((nr, nc))
    return len(trail_end)


def get_trailheads(grid):
    for r, row in enumerate(grid):
        for c, square in enumerate(row):
            if square == 0:
                yield r, c


def main(grid):
    trailheads = get_trailheads(grid)

    counter = 0
    for r, c in trailheads:
        counter += score(r, c, grid)

    return counter


if __name__ == "__main__":
    file_path = sys.argv[1]
    with open(file_path, "r") as f:
        grid = [[int(n) for n in list(l.rstrip())] for l in f]

    print(main(grid))
