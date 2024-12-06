import sys


def right_order(update, ordering):
    for i, page in enumerate(update):
        for next_page in update[i + 1 :]:
            if page in ordering[next_page]:
                return False
    return True


def main(rules, updates):
    ordering = {}
    counter = 0
    for page, next in rules:
        if page not in ordering:
            ordering[page] = {next}
        else:
            ordering[page].add(next)

    for update in updates:
        if right_order(update, ordering):
            mid = len(update) // 2
            counter += int(update[mid])

    return counter


if __name__ == "__main__":
    path_file = sys.argv[1]
    with open(path_file, "r") as f:
        lines = [l.rstrip() for l in f.readlines()]
        line_break = lines.index("")
        rules = [l.split("|") for l in lines[:line_break]]
        updates = [l.split(",") for l in lines[line_break + 1 :]]

    print(main(rules, updates))
