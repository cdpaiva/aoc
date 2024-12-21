from collections import deque
from time import sleep
import sys


def starting_pos(grid):
    for r, row in enumerate(grid):
        for c, square in enumerate(row):
            if square == "@":
                return (r, c)
    raise ValueError("Cannot find the robot's starting position.")


def double_square(line):
    out = ""
    for ch in line:
        if ch == "O":
            out += "[]"
        elif ch == "@":
            out += "@."
        else:
            out += ch * 2
    return out


def main(lines):
    i = lines.index("")
    moves = list("".join(lines[i + 1 :]))
    grid = [list(double_square(l)) for l in lines[:i]]

    r, c = starting_pos(grid)
    directions = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}

    for move in moves:
        for row in grid:
            print("".join(row))
        sleep(0.1)
        dr, dc = directions[move]
        front_block = grid[r + dr][c + dc]

        if front_block == "#":
            continue
        grid[r][c] = "."
        if front_block == ".":
            r += dr
            c += dc
        else:
            nr = r + dr
            nc = c + dc

            if dr == 0:
                # moving vertically:
                moves = 0
                # find contiguous blocks
                while grid[nr][nc] == "[" or grid[nr][nc] == "]":
                    nc += dc
                    moves += 1
                if grid[nr][nc] == "#":
                    grid[r][c] = "@"
                    continue
                elif grid[nr][nc] == ".":
                    # shift all blocks once in direction dc
                    for i in range(moves):
                        grid[nr][nc] = grid[nr][nc - dc]
                        nc -= dc
                    grid[r + dr][c + dc] = "."
                    r += dr
                    c += dc
            else:
                # moving vertically:
                connected_blocks = set()
                border = set()
                q = deque()
                q.appendleft((nr, nc))
                if grid[nr][nc] == "[":
                    q.appendleft((nr, nc + 1))
                elif grid[nr][nc] == "]":
                    q.appendleft((nr, nc - 1))
                while q:
                    cr, cc = q.pop()
                    if grid[cr][cc] == "[" or grid[cr][cc] == "]":
                        connected_blocks.add((cr, cc, grid[cr][cc]))
                        q.appendleft((cr + dr, cc))
                        following = grid[cr + dr][cc]
                        if following == "]":
                            q.appendleft((cr + dr, cc - 1))
                        elif following == "[":
                            q.appendleft((cr + dr, cc + 1))
                        else:
                            border.add((cr + dr, cc, grid[cr + dr][cc]))
                # cb = sorted(list(connected_blocks))
                if all(b[2] == "." for b in border):
                    for cr, cc, orig in connected_blocks:
                        grid[cr][cc] = "."
                    for cr, cc, orig in connected_blocks:
                        grid[cr + dr][cc] = orig
                    r += dr
                    c += dc
                else:
                    grid[r][c] = "@"
                    continue
        grid[r][c] = "@"

    gps = 0
    for r, row in enumerate(grid):
        for c, square in enumerate(row):
            if square == "[":
                gps += r * 100 + c
    return gps


if __name__ == "__main__":
    file_path = sys.argv[1]

    with open(file_path, "r") as f:
        lines = [l.rstrip() for l in f]

    print(main(lines))
