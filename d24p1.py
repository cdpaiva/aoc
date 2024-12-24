import sys


def main(computed, state):
    num_of_gates = len(computed) + len(state)

    ops = dict(AND="&", OR="|", XOR="^")

    while len(computed) < num_of_gates:
        for gate, (op1, op2, operand) in state.items():
            if gate in computed:
                continue
            if op1 in computed and op2 in computed:
                computed[gate] = eval(f"{computed[op1]} {ops[operand]} {computed[op2]}")

    out = 0
    z_gates = list(k for k in computed.keys() if k.startswith("z"))
    for k in sorted(z_gates, reverse=True):
        out = out * 2 + computed[k]
    return out


if __name__ == "__main__":
    file_path = sys.argv[1]

    with open(file_path, "r") as f:
        initial_values, gates = f.read().split("\n\n")

        computed = {}
        for line in initial_values.split("\n"):
            k, v = line.split(": ")
            computed[k] = int(v)

        state = {}
        for line in gates.split("\n"):
            if line == "":
                continue
            rule, gate = line.split(" -> ")
            operand1, operator, operand2 = rule.split(" ")
            state[gate] = (operand1, operand2, operator)

    print(main(computed, state))
