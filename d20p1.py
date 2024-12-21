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

    max_dist = 0
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

    # calculate shorcut distances
    seen = set()
    q = deque()
    q.append((sr, sc))
    counter = 0
    shortcuts = []

    while q:
        r, c = q.pop()
        seen.add((r, c))
        if grid[r][c] == "E":
            break
        for dr, dc in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            nr, nc = r + dr, c + dc
            if grid[nr][nc] == "#":
                tr, tc = nr + dr, nc + dc
                if tr < 0 or tr >= rows or tc < 0 or tc >= cols:
                    continue
                if grid[tr][tc] == "." or grid[tr][tc] == "E" and (tr, tc) not in seen:
                    if distances[(r, c)] - distances[(tr, tc)] >= 102:
                        shortcuts.append(distances[(r, c)] - distances[(tr, tc)] - 2)
                        counter += 1
            if grid[nr][nc] == "." and (nr, nc) not in seen:
                q.appendleft((nr, nc))

    return counter


if __name__ == "__main__":
    file_path = sys.argv[1]

    with open(file_path, "r") as f:
        grid = [list(l.rstrip()) for l in f]

    print(main(grid))
