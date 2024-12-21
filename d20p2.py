from collections import deque, Counter
import sys


def get_starting_pos(grid):
    for r, row in enumerate(grid):
        for c, square in enumerate(row):
            if square == "S":
                return (r, c)
    raise ValueError("Cannot find starting position.")


def main(grid):
    rows = len(grid)
    cols = len(grid[0])

    sr, sc = get_starting_pos(grid)

    # calculate all distances to the end
    distances = {}
    seen = set()
    q = deque()
    q.append((sr, sc, 0))

    while q:
        r, c, dist = q.pop()
        seen.add((r, c))
        distances[(r, c)] = dist
        if grid[r][c] == "E":
            break
        for dr, dc in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            nr, nc = r + dr, c + dc
            if (grid[nr][nc] == "." or grid[nr][nc] == "E") and (nr, nc) not in seen:
                q.appendleft((nr, nc, dist + 1))

    max_dist = distances[(r, c)]
    distances = {k: max_dist - v for k, v in distances.items()}

    counter = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '#':
                continue
            for radius in range(2, 21):
                for dr in range(radius + 1):
                    dc = radius - dr
                    for nr, nc in {(r+dr, c+dc), (r+dr, c-dc), (r-dr, c+dc), (r-dr, c-dc)}:
                        if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                            continue
                        if grid[nr][nc] == '#':
                            continue
                        if distances[(r, c)] - distances[(nr, nc)] >= 100 + radius:
                            counter += 1
    return counter


if __name__ == "__main__":
    file_path = sys.argv[1]

    with open(file_path, "r") as f:
        grid = [list(l.rstrip()) for l in f]

    print(main(grid))
