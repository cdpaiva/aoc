from collections import defaultdict
import sys


def main(conns):
    nodes = defaultdict(list)

    for conn in conns:
        a, b = conn.split("-")
        nodes[a].append(b)
        nodes[b].append(a)

    max_len = 0
    max_clique = []
    for start in nodes:
        clique = [start]
        for n in nodes:
            if n == start:
                continue
            if all(n in nodes[c] for c in clique):
                clique.append(n)
        if len(clique) > max_len:
            max_len = len(clique)
            max_clique = clique[:]

    return ",".join(sorted(max_clique))


if __name__ == "__main__":
    file_path = sys.argv[1]

    with open(file_path, "r") as f:
        conns = [l.rstrip() for l in f]

    print(main(conns))
