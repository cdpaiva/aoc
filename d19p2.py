import sys

cache = {}


def main(towels, combinations):

    def num_combinations(comb):
        if not comb:
            return 1
        if comb in cache:
            return cache[comb]

        total = sum(
            [num_combinations(comb[len(t) :]) for t in towels if comb.startswith(t)]
        )

        cache[comb] = total
        return total

    return sum(num_combinations(comb) for comb in combinations)


if __name__ == "__main__":
    file_path = sys.argv[1]

    with open(file_path, "r") as f:
        lines = [l.rstrip() for l in f]

    towels = {t for t in lines[0].split(", ")}
    combinations = lines[2:]

    print(main(towels, combinations))
