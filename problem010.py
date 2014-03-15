import math

limit = 2000000

not_prime = []

def is_prime(n):
    if n in not_prime:
        return False

    i = 2
    while i < n:
        if (n % i != 0):
            not_prime.append(n)
            return False
        i += 1
    return True

def main():
    i = 2
    total = 0

    while i < limit:
        print i
        if is_prime(i):
            total += i

        i += 1

    print total

if __name__ == '__main__':
  main()
