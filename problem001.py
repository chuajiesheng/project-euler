def main():
    max = 1000
    total = 0
    i = 0

    while(i < max):
        if (i % 3 == 0):
            total += i
        elif (i % 5 == 0):
            total += i
        i += 1

    print total

if __name__ == '__main__':
  main()
