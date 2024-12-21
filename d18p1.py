from collections import deque
import sys


def main(byte_pos, num_bytes, rows=7, cols=7):
    target = (rows-1, cols-1)
    grid = [['.']*cols for _ in range(rows)]

    for c, r in byte_pos[:num_bytes]:
        grid[r][c] = '#'

    seen = set()
    q = deque()
    q.appendleft((0, 0, 0))
    while q:
        r, c, dist = q.pop()
        if (r, c) == target:
            return dist
        if grid[r][c] == '#' or (r, c) in seen:
            continue
        seen.add((r, c))
        for dr, dc in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            nr = r + dr
            nc = c + dc
            if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                continue
            if grid[r][c] == '.':
                q.appendleft((nr, nc, dist+1))

    raise ValueError('Could not reach target position')


if __name__ == '__main__':
    file_path = sys.argv[1]

    with open(file_path, 'r') as f:
        byte_pos = [[int(n) for n in l.rstrip().split(',')] for l in f]

    print(main(byte_pos, num_bytes=1024, rows=71, cols=71))
