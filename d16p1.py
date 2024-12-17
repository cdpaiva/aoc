import networkx as nx
import sys


def walk(r, c, dr, dc, grid, nodes):
    dirs = ((-1, 0), (0, 1), (1, 0), (0, -1))
    seen = set()
    seen.add((r, c))
    r += dr
    c += dc
    cost = 1
    while (r, c) not in nodes:
        seen.add((r, c))
        if grid[r + dr][c + dc] == ".":
            cost += 1
            r += dr
            c += dc
        else:
            for ndr, ndc in dirs:
                nr = r + ndr
                nc = c + ndc
                if (nr, nc) in seen:
                    continue
                if grid[nr][nc] == ".":
                    cost += 1001
                    dr = ndr
                    dc = ndc
                    r += dr
                    c += dc
                    break
    return ((r, c, dr, dc), cost)


def main(grid):
    nodes = []

    dirs = ((-1, 0), (0, 1), (1, 0), (0, -1))
    for r, row in enumerate(grid):
        for c, square in enumerate(row):
            if square == ".":
                num_paths = sum(
                    1 for (ndr, ndc) in dirs if grid[r + ndr][c + ndc] == "."
                )
                if num_paths > 2 or num_paths == 1:
                    nodes.append((r, c))
            if square == "S" or square == "E":
                nodes.append((r, c))
                grid[r][c] = "."

    graph = 0

    graph = {}
    for r, c in nodes:
        for ndr, ndc in dirs:
            graph[r, c, ndr, ndc] = []
            if ndc == 0:
                graph[r, c, ndr, ndc].append(((r, c, 0, -1), 1000))
                graph[r, c, ndr, ndc].append(((r, c, 0, 1), 1000))
            if ndr == 0:
                graph[r, c, ndr, ndc].append(((r, c, -1, 0), 1000))
                graph[r, c, ndr, ndc].append(((r, c, 1, 0), 1000))
            if grid[r + ndr][c + ndc] != "#":
                graph[r, c, ndr, ndc].append(walk(r, c, ndr, ndc, grid, nodes))

    G = nx.Graph()

    for node, edges in graph.items():
        for other, cost in edges:
            G.add_edge(str(node), str(other), weight=cost)

    weights = {}
    for n1, n2, w in G.edges(data=True):
        weights[n1, n2] = w["weight"]
        weights[n2, n1] = w["weight"]

    cost_1 = 0
    path = nx.shortest_path(G, "(139, 1, 0, 1)", "(1, 139, -1, 0)", weight="weight")

    path_edges = list(zip(path, path[1:]))
    for pe in path_edges:
        cost_1 += weights[pe]

    cost_2 = 0
    path = nx.shortest_path(G, "(139, 1, 0, 1)", "(1, 139, 0, 1)", weight="weight")

    path_edges = list(zip(path, path[1:]))
    for pe in path_edges:
        cost_2 += weights[pe]

    return min(cost_1, cost_2)


if __name__ == "__main__":
    file_path = sys.argv[1]

    with open(file_path, "r") as f:
        grid = [list(l.rstrip()) for l in f]

    print(main(grid))
