from collections import defaultdict
import sys


def main(conns):
    nodes = defaultdict(list)

    for conn in conns:
        a, b = conn.split("-")
        nodes[a].append(b)
        nodes[b].append(a)

    groups = set()
    for node, neighbors in nodes.items():
        if not node.startswith("t"):
            continue
        for nn in neighbors:
            # a neighbor of the current node's neighbors must be a neighbor of the
            # current node too, then they form a set of three connected nodes.
            for nnn in nodes[nn]:
                if nnn in nodes[node]:
                    groups.add(tuple(sorted((node, nn, nnn))))
    return len(groups)


if __name__ == "__main__":
    file_path = sys.argv[1]

    with open(file_path, "r") as f:
        conns = [l.rstrip() for l in f]

    print(main(conns))
