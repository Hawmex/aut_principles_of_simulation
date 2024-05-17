import math


def isPower(num, base):
    return math.log(num, base) % 1 == 0


def isPrime(n):
    # https://stackoverflow.com/a/15285588/7330316
    if n < 2 or n % 2 == 0:
        return False
    if n == 2 or n == 3:
        return True
    if n < 9:
        return True
    if n % 3 == 0:
        return False

    f = 5
    while f <= int(n**0.5):
        if n % f == 0:
            return False
        if n % (f + 2) == 0:
            return False
        f += 6
    return True
