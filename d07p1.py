import sys


def combinable(nums, target):
    num_perms = 1 << (len(nums) - 1)

    for i in range(num_perms):
        acc = nums[0]
        for j, num in enumerate(nums[1:]):
            if i & (1 << j):
                acc *= num
            else:
                acc += num
        if acc == target:
            return True
    return False


def main(lines):
    counter = 0
    for line in lines:
        target, rest = line.split(": ")
        target = int(target)
        nums = [int(n) for n in rest.split()]
        counter += target if combinable(nums, target) else 0
    return counter


if __name__ == "__main__":
    file_path = sys.argv[1]

    with open(file_path, "r") as f:
        lines = [l.rstrip() for l in f.readlines()]

    print(main(lines))
