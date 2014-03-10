def is_prime(x):
    n = 2

    while n < x:
        if x % n == 0:
            return False
        n = n + 1

    return True

def main():
    i = 0
    n = 2

    while i < 10002:
        if is_prime(n):
            i = i + 1
        if i == 10001:
            print n
            break
        n = n + 1

if __name__ == '__main__':
  main()
