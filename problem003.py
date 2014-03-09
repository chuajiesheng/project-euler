primes = [1, 2, 3]
number = 600851475143

def is_prime(n):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    max_divisor = int(n ** 0.5) # square root of n
    divisor = 5
    while divisor <= max_divisor:
        if n % divisor == 0 or n % (divisor + 2) == 0:
            return False
        divisor += 6
    return True

def check_prime(n):
    if n in primes:
        return True
    elif is_prime(n):
        primes.append(n)
        return True
    else:
        return False

def main():
    n = 3
    largest_prime_factor = 1

    while n < number:
        if number % n == 0 and check_prime(n):
            largest_prime_factor = n
        n = n + 1

    print_int(largest_prime_factor)

if __name__ == '__main__':
  main()
