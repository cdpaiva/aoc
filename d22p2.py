import sys


def predict(n, times=2000):
    prices = [n % 10]
    while times > 0:
        n = ((n * 64) ^ n) % 16777216
        n = ((n // 32) ^ n) % 16777216
        n = ((n * 2048) ^ n) % 16777216
        prices.append(n % 10)
        times -= 1
    return prices


def main(secret_numbers):
    prices = [predict(n) for n in secret_numbers]

    seq_to_price = {}

    for price in prices:
        diff = [b - a for a, b in zip(price[:-1], price[1:])]
        seen = set()
        for i in range(len(diff)-3):
            seq = tuple(diff[i:i+4])
            if seq in seen:
                continue
            if seq not in seq_to_price:
                seq_to_price[seq] = price[i+4]
            else:
                seq_to_price[seq] += price[i+4]
            seen.add(seq)

    return max(seq_to_price.values())


if __name__ == '__main__':
    file_path = sys.argv[1]

    with open(file_path, 'r') as f:
        secret_numbers = [int(l.rstrip()) for l in f]

    print(main(secret_numbers))
