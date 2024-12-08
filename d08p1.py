import sys


def check_antinodes(coords, rows, cols):
    antinodes = set()
    for i, (r, c) in enumerate(coords):
        for (r2, c2) in coords[i + 1 :]:
            dr = r2 - r
            dc = c2 - c
            # if we are moving in the wrong direction, flip
            if r + dr == r2:
                dr *= -1
                dc *= -1
            # antinode 1:
            ar = r + dr
            ac = c + dc
            if 0 <= ar < rows and 0 <= ac < cols:
                antinodes.add((ar, ac))
            # antinode 2:
            ar = r + -2 * dr
            ac = c + -2 * dc
            if 0 <= ar < rows and 0 <= ac < cols:
                antinodes.add((ar, ac))
    return antinodes


def get_antenna_coords(grid):
    coords = {}
    for r, row in enumerate(grid):
        for c, square in enumerate(row):
            if square == ".":
                continue
            if square in coords:
                coords[square].append((r, c))
            else:
                coords[square] = [(r, c)]
    return coords


def main(grid):
    rows = len(grid)
    cols = len(grid[0])
    antenna_coords = get_antenna_coords(grid)

    antinodes = set()
    for coords in antenna_coords.values():
        antinodes |= check_antinodes(coords, rows, cols)

    return len(antinodes)


if __name__ == "__main__":
    file_path = sys.argv[1]

    with open(file_path, "r") as f:
        grid = [list(l.rstrip()) for l in f]

    print(main(grid))
