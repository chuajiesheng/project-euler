number = 600851475143

def prime_factors(n):
    factors = []
    d = 2

    while n > 1:
        while n % d == 0:
            factors.append(d)
            n = n / d
        d = d + 1
        if d * d > n:
            if n > 1:
                factors.append(n)
            break

    return factors

def main():
    factors = prime_factors(number)
    largest_prime_factor = max(factors)
    print largest_prime_factor

if __name__ == '__main__':
  main()
