import sys


def main(codes):
    keypad_rows = ["789", "456", "123", "X0A"]
    keypad = [list(row) for row in keypad_rows]

    keypad_coords = {}
    for r, row in enumerate(keypad):
        for c, square in enumerate(row):
            keypad_coords[square] = (r, c)

    dirs = {
        "A": {"A": "", "^": "<", "v": "v<", "<": "v<<", ">": "v"},
        "^": {"A": ">", "^": "", "v": "v", "<": "v<", ">": "v>"},
        "v": {"A": "^>", "^": "^", "v": "", "<": "<", ">": ">"},
        "<": {"A": ">>^", "^": "^>", "v": ">", "<": "", ">": ">>"},
        ">": {"A": "^", "^": "^<", "v": "<", "<": "<<", ">": ""},
    }

    seqs = []
    for code in codes:
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

        out = ""
        move = "A" + move
        for (s, e) in zip(move[:-1], move[1:]):
            out += dirs[s][e] + "A"

        move = "A" + out
        out = ""
        for (s, e) in zip(move[:-1], move[1:]):
            out += dirs[s][e] + "A"

        seqs.append(out)

    complexity = 0
    for c, s in zip(codes, seqs):
        print(len(s))
        complexity += int(c[:-1]) * len(s)

    return complexity


if __name__ == "__main__":
    file_path = sys.argv[1]

    with open(file_path, "r") as f:
        codes = [l.rstrip() for l in f]

    print(main(codes))
