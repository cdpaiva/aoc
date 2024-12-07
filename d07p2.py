import sys


def combinable(nums, target):
    num_perms = 3 ** (len(nums) - 1)
    for i in range(num_perms):
        acc = nums[0]
        flag = i
        for num in nums[1:]:
            if flag % 3 == 0:
                acc *= num
            elif flag % 3 == 1:
                acc += num
            else:
                acc = int(str(acc) + str(num))
            flag //= 3
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
