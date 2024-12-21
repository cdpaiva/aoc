from collections import deque
import sys


def is_corner(r, c, grid, plant):
    rows = len(grid)
    cols = len(grid[0])
    neighbors = ((-1, -1), (-1, 0), (0, -1), (0, 0))  # top left corner
    # plant = grid[r][c]

    empty_sides = []
    for i, (dr, dc) in enumerate(neighbors):
        cr = r + dr
        cc = c + dc
        # print(f"Checking on {cr, cc}")
        if cr < 0 or cr >= rows or cc < 0 or cc >= cols:
            empty_sides.append(i)
        elif grid[cr][cc] != plant:
            empty_sides.append(i)

    # print(f"Top left corner of {r,c} has {len(empty_sides)} empty sides. ")
    if len(empty_sides) == 1 or len(empty_sides) == 3:
        return True
    if len(empty_sides) == 4:
        return False
    if len(empty_sides) == 2:
        if empty_sides == [0, 3] or empty_sides == [1, 2]:
            return True
        return False


def find_regions(grid):
    # total = 0
    visited = set()
    rows = len(grid)
    cols = len(grid[0])
    # corners = 0
    regions = {}

    neighbors = ((-1, 0), (0, 1), (1, 0), (0, -1))  # N, W, S, E
    for r, row in enumerate(grid):
        for c, plant in enumerate(row):
            if (r, c) in visited:
                continue
            else:
                region_coords = set()
                q = deque()
                q.append((r, c))
                area = 0
                while q:
                    cr, cc = q.pop()
                    if grid[cr][cc] != plant or (cr, cc) in visited:
                        continue
                    visited.add((cr, cc))
                    region_coords.add((cr, cc))
                    area += 1
                    for dr, dc in neighbors:
                        # count CORNERs instead of sides
                        nr = cr + dr
                        nc = cc + dc
                        if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                            continue
                        elif grid[nr][nc] != plant:
                            continue
                        else:
                            q.append((nr, nc))
                # total += area
                regions[(r, c)] = {"area": area, "visited": region_coords}
            # print(f"Visited {r, c} [{grid[r][c]}] => area = {area}")
    return regions


def main(grid):
    regions = find_regions(grid)

    counter = 0
    for (o_r, o_c), region in regions.items():
        plant = grid[o_r][o_c]
        num_corners = 0
        buffer = set()
        for r, c in region["visited"]:
            buffer.add((r + 1, c))
            buffer.add((r, c + 1))
            buffer.add((r + 1, c + 1))
        new_region = region["visited"].union(buffer)
        for r, c in new_region:
            # print(f"Checking corners in {r, c} [{grid[r][c]}]")
            num_corners += 1 if is_corner(r, c, grid, plant) else 0
        print(f"Area {r,c} has {num_corners} corners.")
        counter += region["area"] * num_corners

    return counter


if __name__ == "__main__":
    file_path = sys.argv[1]

    with open(file_path, "r") as f:
        grid = [list(l.rstrip()) for l in f]

    print(main(grid))
