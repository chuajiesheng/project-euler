def is_palindrome(n):
    s = list(str(n))

    is_palindrome = True
    for i in range(len(s) / 2):
        if s[i] != s[len(s) - i - 1]:
            is_palindrome = False

    return is_palindrome

def main():
    x = 900
    y = 900

    n = x * y

    while x < 1000:
        while y < 1000:
            if is_palindrome(n):
                print n
            y = y + 1
            n = n + x
        x = x + 1
        y = 900
        n = x * y

if __name__ == '__main__':
  main()
