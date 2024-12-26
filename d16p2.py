from collections import defaultdict
from heapq import heappush, heappop
import sys


def main(grid):
    rows = len(grid)
    # starting pos and direction
    sr, sc = rows - 2, 1
    sdr, sdc = 0, 1

    q = [(0, sr, sc, sdr, sdc)]
    seen = {(sr, sc, sdr, sdc)}

    min_dists = defaultdict(lambda: float("inf"))

    previous = {}
    final_pos = (0, 0, 0, 0)

    while q:
        dist, r, c, dr, dc = heappop(q)
        seen.add((r, c, dr, dc))

        if grid[r][c] == "E":
            final_pos = r, c, dr, dc
            break

        # move forward:
        nr, nc = r + dr, c + dc
        new_dist = dist + 1
        if grid[nr][nc] != "#":
            if new_dist > min_dists[(nr, nc, dr, dc)]:
                continue
            if new_dist < min_dists[(nr, nc, dr, dc)]:
                previous[(nr, nc, dr, dc)] = set()
                min_dists[(nr, nc, dr, dc)] = new_dist
            previous[(nr, nc, dr, dc)].add((r, c, dr, dc))
            heappush(q, (new_dist, nr, nc, dr, dc))

        # rotate:
        if dr == 0:
            dirs = ((-1, 0), (1, 0))
        else:
            dirs = ((0, -1), (0, 1))

        for (ndr, ndc) in dirs:
            nr, nc = r + ndr, c + ndc
            new_dist = dist + 1000
            if grid[nr][nc] != "#":
                if new_dist > min_dists[(r, c, ndr, ndc)]:
                    continue
                if new_dist < min_dists[(r, c, ndr, ndc)]:
                    previous[(r, c, ndr, ndc)] = set()
                    min_dists[(r, c, ndr, ndc)] = new_dist
                previous[(r, c, ndr, ndc)].add((r, c, dr, dc))
                heappush(q, (new_dist, r, c, ndr, ndc))

    states = [final_pos]
    seen = set()

    while states:
        key = states.pop()
        for last in previous.get(key, []):
            if last in seen:
                continue
            seen.add(last)
            states.append(last)

    squares = {(r, c) for r, c, _, _ in seen}
    # add 1 for the final square
    return len(squares) + 1


if __name__ == "__main__":
    file_path = sys.argv[1]

    with open(file_path, "r") as f:
        grid = [list(l.rstrip()) for l in f]

    print(main(grid))
