import sys

from d08p1 import get_antenna_coords


def check_antinodes(coords, rows, cols):
    antinodes = set()
    for i, (r, c) in enumerate(coords):
        for r2, c2 in coords[i + 1 :]:
            antinodes.add((r, c))
            dr = r2 - r
            dc = c2 - c
            # move in one direction
            ar = r + dr
            ac = c + dc
            # while we are still in the grid, add points
            while 0 <= ar < rows and 0 <= ac < cols:
                antinodes.add((ar, ac))
                ar += dr
                ac += dc

            # move in opposite direction
            ar = r - dr
            ac = c - dc
            # while we are still in the grid, add points
            while 0 <= ar < rows and 0 <= ac < cols:
                antinodes.add((ar, ac))
                ar -= dr
                ac -= dc

    return antinodes


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
