from heapq import heappush, heappop
import sys


def main(grid):
    rows = len(grid)

    q = [(0, rows - 2, 1, 0, 1)]
    seen = {(rows - 2, 1, 0, 1)}

    while q:
        dist, r, c, dr, dc = heappop(q)
        seen.add((r, c, dr, dc))
        if grid[r][c] == "E":
            return dist

        # move forward:
        nr, nc = r + dr, c + dc
        if (nr, nc, dr, dc) in seen:
            continue
        if grid[nr][nc] != "#":
            heappush(q, (dist + 1, nr, nc, dr, dc))

        # rotate:
        if dr == 0:
            dirs = ((-1, 0), (1, 0))
        else:
            dirs = ((0, -1), (0, 1))

        for (ndr, ndc) in dirs:
            nr, nc = r + ndr, c + ndc
            if (nr, nc, dr, dc) in seen:
                continue
            if grid[nr][nc] != "#":
                heappush(q, (dist + 1000, r, c, ndr, ndc))

    raise ValueError("Could not reach target")


if __name__ == "__main__":
    file_path = sys.argv[1]

    with open(file_path, "r") as f:
        grid = [list(l.rstrip()) for l in f]

    print(main(grid))
