from collections import deque
import sys


def main(grid):
    total = 0
    visited = set()
    rows = len(grid)
    cols = len(grid[0])

    neighbors = ((-1, 0), (0, 1), (1, 0), (0, -1))  # N, W, S, E
    for r, row in enumerate(grid):
        for c, plant in enumerate(row):
            if (r, c) in visited:
                continue
            else:
                q = deque()
                q.append((r, c))
                area = 0
                per = 0
                while q:
                    cr, cc = q.pop()
                    if grid[cr][cc] != plant or (cr, cc) in visited:
                        continue
                    visited.add((cr, cc))
                    area += 1
                    for dr, dc in neighbors:
                        nr = cr + dr
                        nc = cc + dc
                        if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                            per += 1
                            continue
                        elif grid[nr][nc] != plant:
                            per += 1
                            continue
                        else:
                            q.append((nr, nc))
                total += area * per
    return total


if __name__ == "__main__":
    file_path = sys.argv[1]

    with open(file_path, "r") as f:
        grid = [list(l.rstrip()) for l in f]

    print(main(grid))
