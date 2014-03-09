def sum_square(n):
    total = 0
    numbers = range(1, n + 1)

    for n in numbers:
        total += n ** 2

    return total

def square_sum(n):
    total = 0
    numbers = range(1, n + 1)

    for n in numbers:
        total += n

    return total ** 2

def main():
    diff = square_sum(100) - sum_square(100)
    print diff


if __name__ == '__main__':
  main()
