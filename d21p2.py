import sys


def dirs_from_keypad(code):
    keypad_rows = ["789", "456", "123", "X0A"]
    keypad = [list(row) for row in keypad_rows]
    keypad_coords = {}
    for r, row in enumerate(keypad):
        for c, square in enumerate(row):
            keypad_coords[square] = (r, c)

    code = "A" + code
    move = ""

    for (s, e) in zip(code[:-1], code[1:]):
        sr, sc = keypad_coords[s]
        er, ec = keypad_coords[e]
        dr = er - sr
        dc = ec - sc

        vert_move = "v" * dr if dr > 0 else "^" * abs(dr)
        horiz_move = ">" * dc if dc > 0 else "<" * abs(dc)

        if ec > sc and (er, sc) != (3, 0):
            move += vert_move + horiz_move
        elif (sr, ec) != (3, 0):
            move += horiz_move + vert_move
        else:
            move += vert_move + horiz_move

        move += "A"
    return move


def shortest_path_dir(move):
    dirs = {
        "A": {"A": "A", "^": "<A", "v": "<vA", "<": "v<<A", ">": "vA"},
        "^": {"A": ">A", "^": "A", "v": "vA", "<": "v<A", ">": "v>A"},
        "<": {"A": ">>^A", "^": ">^A", "v": ">A", "<": "A", ">": ">>A"},
        "v": {"A": "^>A", "^": "^A", "v": "A", "<": "<A", ">": ">A"},
        ">": {"A": "^A", "^": "<^A", "v": "<A", "<": "<<A", ">": "A"},
    }

    out = []
    for (s, e) in zip(move[:-1], move[1:]):
        out.append(dirs[s][e])

    return out


def main(codes):
    complexity = 0
    for code in codes:
        move = dirs_from_keypad(code)

        pair_freq = {}
        pair_freq[move] = 1

        for _ in range(25):
            new_freqs = {}
            for seq, freq in pair_freq.items():
                seq = "A" + seq
                new_pairs = shortest_path_dir(seq)
                for np in new_pairs:
                    new_freqs[np] = new_freqs.get(np, 0) + freq
                pair_freq = new_freqs

        cost = sum(len(k) * v for k, v in pair_freq.items())
        complexity += int(code[:-1]) * cost

    return complexity


if __name__ == "__main__":
    file_path = sys.argv[1]

    with open(file_path, "r") as f:
        codes = [l.rstrip() for l in f]

    print(main(codes))
