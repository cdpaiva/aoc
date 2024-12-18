import sys


def main(reg_a, reg_b, reg_c, program):
    combo = {0: 0, 1: 1, 2: 2, 3: 3, 4: reg_a, 5: reg_b, 6: reg_c, 7: None}

    out = ""
    ptr = 0

    while ptr < len(program):
        opcode = program[ptr]
        operand = program[ptr + 1]
        if opcode == 0:
            reg_a = reg_a // (2 ** combo[operand])
        elif opcode == 1:
            reg_b = reg_b ^ operand
        elif opcode == 2:
            reg_b = combo[operand] % 8
        elif opcode == 3:
            if reg_a != 0:
                ptr = operand - 2
        elif opcode == 4:
            reg_b = reg_b ^ reg_c
        elif opcode == 5:
            out += str(combo[operand] % 8) + ","
        elif opcode == 6:
            reg_b = reg_a // (2 ** combo[operand])
        elif opcode == 7:
            reg_c = reg_a // (2 ** combo[operand])
        else:
            raise ValueError("Invalid opcode.")
        ptr += 2
        combo = {0: 0, 1: 1, 2: 2, 3: 3, 4: reg_a, 5: reg_b, 6: reg_c, 7: None}

    return reg_a, reg_b, reg_c, program, out


if __name__ == "__main__":
    file_path = sys.argv[1]

    with open(file_path, "r") as f:
        lines = [l.rstrip().split(": ")[-1] for l in f if l != "\n"]

    reg_a, reg_b, reg_c, program = lines

    program = [int(opcode) for opcode in program.split(",")]

    out = main(int(reg_a), int(reg_b), int(reg_c), program)

    print(out[-1])
