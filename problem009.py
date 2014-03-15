import math

abc = 1000

def check_pythagorean_triplet(a, b, c):
    return math.pow(c, 2) == (math.pow(a, 2) + math.pow(b, 2))

def product(a, b, c):
    return a * b * c

def check_requirement(a, b, c):
    return (a + b + c) == abc

def main():
    a = 1
    b = 2

    while a < abc:
        while b < (abc - a - b):
            if check_requirement(a, b, abc - a- b):
                if check_pythagorean_triplet(a, b, abc - a - b):
                    print a, b, abc - a -b, product(a, b, abc - a - b)
                    break

            b += 1

        a += 1
        b = a + 1

if __name__ == '__main__':
  main()
