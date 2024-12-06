import sys


def correct(update, ordering):
    corrected = []

    for page in update:
        was_inserted = False
        for i, el in enumerate(corrected[:]):
            if el in ordering and page in ordering[el]:
                continue
            else:
                was_inserted = True
                corrected.insert(i, page)
                break
        if not was_inserted:
            corrected.append(page)

    return corrected


def is_ordered(update, ordering):
    for i, page in enumerate(update):
        for next in update[i + 1 :]:
            if next in ordering and page in ordering[next]:
                return False
    return True


def main(rules, updates):
    ordering = {}
    for page, next in rules:
        if page not in ordering:
            ordering[page] = {next}
        else:
            ordering[page].add(next)
    counter = 0
    for update in updates:
        if not is_ordered(update, ordering):
            corrected = correct(update, ordering)
            counter += int(corrected[len(corrected) // 2])
    return counter


if __name__ == "__main__":
    file_path = sys.argv[1]
    with open(file_path, "r") as f:
        lines = [l.rstrip() for l in f.readlines()]
        line_break = lines.index("")
        rules = [l.split("|") for l in lines[:line_break]]
        updates = [l.split(",") for l in lines[line_break + 1 :]]

    print(main(rules, updates))
