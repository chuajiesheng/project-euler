import math

def get_factors(num):
    factors = [1]
    i = 2

    while i < math.sqrt(num):
        if num % i == 0:
            factors.append(i)
            factors.append(num / i)
        i = i + 1

    if i * i == num:
        factors.append(i)

    return factors

def main():
    t = 1
    i = 2

    while True:
        factors = get_factors(t)
        if len(factors) > 500:
            print t, "has ", len(factors), "factors. ", factors
            break
        t = t + i
        i = i + 1

if __name__ == '__main__':
  main()
