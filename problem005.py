def main():
    x = 2520 * 11 * 13 * 17 * 19
    factor = range(1, 21)
    max = 1
    for n in factor:
        max = max * n

    while x <= max:
        found = True
        for n in factor:
            if x % n != 0:
                found = False
                break

        if found:
            print x
            break

        x = x + 1

if __name__ == '__main__':
  main()
