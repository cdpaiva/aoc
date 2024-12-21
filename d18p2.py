from collections import deque
import sys


def main(byte_pos, rows=7, cols=7):
    target = (rows-1, cols-1)
    grid = [['.']*cols for _ in range(rows)]

    for c, r in byte_pos:
        orig_coords = (c, r)
        print(c, r)
        grid[r][c] = '#'

        seen = set()
        q = deque()
        q.appendleft((r, c))

        while q:
            r, c = q.pop()
            if grid[r][c] == '.' or (r, c) in seen:
                continue
            seen.add((r, c))
            for dr, dc in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)):
                nr = r + dr
                nc = c + dc
                if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                    continue
                if grid[r][c] == '#':
                    q.appendleft((nr, nc))

        seen = sorted(list(seen))
        max_r = seen[-1]
        min_r = seen[0]
        seen_col = sorted(seen, key=lambda pos: pos[1])
        max_c = seen_col[-1]
        min_c = seen_col[0]

        print(max_r, min_r, max_c, min_c)

        score = 0
        if max_r[0] == rows - 1:
            score += 1
        if max_c[1] == cols - 1:
            score += 1
        if min_c[1] == 0:
            score += 1
        if min_r[0] == 0:
            score += 1

        if score >= 2:
            # check regular BFS
            solvable = False
            seen = set()
            q = deque()
            q.appendleft((0, 0))
            while q:
                r, c = q.pop()
                if (r, c) == target:
                    solvable = True
                    break
                if grid[r][c] == '#' or (r, c) in seen:
                    continue
                seen.add((r, c))
                for dr, dc in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                    nr = r + dr
                    nc = c + dc
                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                        continue
                    if grid[r][c] == '.':
                        q.appendleft((nr, nc))

            if not solvable:
                return orig_coords

    raise ValueError('Could not reach target position')


if __name__ == '__main__':
    file_path = sys.argv[1]

    with open(file_path, 'r') as f:
        byte_pos = [[int(n) for n in l.rstrip().split(',')] for l in f]

    # print(main(byte_pos))
    print(main(byte_pos, rows=71, cols=71))
