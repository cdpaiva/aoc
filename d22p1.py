import sys


def predict(n, times=2000):
    while times > 0:
        n = ((n * 64) ^ n) % 16777216
        n = ((n // 32) ^ n) % 16777216
        n = ((n * 2048) ^ n) % 16777216
        times -= 1
    return n


def main(secret_numbers):
    return sum([predict(n) for n in secret_numbers])


if __name__ == '__main__':
    file_path = sys.argv[1]

    with open(file_path, 'r') as f:
        secret_numbers = [int(l.rstrip()) for l in f]

    print(main(secret_numbers))
