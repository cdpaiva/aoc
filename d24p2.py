import sys


def process(op, op1, op2):
    if op == "AND":
        return op1 & op2
    elif op == "OR":
        return op1 | op2
    elif op == "XOR":
        return op1 ^ op2


def main(operations):
    wrong = set()
    for op1, op, op2, res in operations:
        if res[0] == "z" and op != "XOR" and res != highest_z:
            wrong.add(res)
        if (
            op == "XOR"
            and res[0] not in ["x", "y", "z"]
            and op1[0] not in ["x", "y", "z"]
            and op2[0] not in ["x", "y", "z"]
        ):
            wrong.add(res)
        if op == "AND" and "x00" not in [op1, op2]:
            for subop1, subop, subop2, _ in operations:
                if (res == subop1 or res == subop2) and subop != "OR":
                    wrong.add(res)
        if op == "XOR":
            for subop1, subop, subop2, _ in operations:
                if (res == subop1 or res == subop2) and subop == "OR":
                    wrong.add(res)
    return ",".join(sorted(wrong))


if __name__ == "__main__":
    file_path = sys.argv[1]

    with open(file_path, "r") as f:
        operations = []
        highest_z = "z00"
        data = [l.rstrip() for l in f]
        for line in data:
            if "->" in line:
                op1, op, op2, _, res = line.split(" ")
                operations.append((op1, op, op2, res))
                if res[0] == "z" and int(res[1:]) > int(highest_z[1:]):
                    highest_z = res

    print(main(operations))
