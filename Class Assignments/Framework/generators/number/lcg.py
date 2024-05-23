from numba import njit
import numpy as np
from helpers import isPower, isPrime


@njit
def lcg_yield(seed, a, c, m):
    x = seed

    while True:
        next_x = (x * a + c) % m

        yield next_x / m
        x = next_x


@njit
def lcg(seed, a, c, m, limit):
    R = np.empty(limit)
    x = seed
    for i in range(limit):
        x = (x * a + c) % m
        R[i] = x / m
    return R


# because @njit has problem with 'limit=None' default value
def generate(seed, a, c, m, limit=None):
    if limit is None:
        limit = m
    return lcg(seed, a, c, m, limit)


# c = 0: multiplicative,
# c != 0: mixed


def findMaxPeriod(seed, a, c, m):
    if isPower(m, 2):
        if c != 0:
            print("c should be prime to m, a becomes 1 + 4k")
        #         P = m
        if c == 0:
            print("yes")
    #         x0 should be odd
    #         a should be 3+8k or 5+8k
    #         P = m/4 = 2**(b-2)
    if isPrime(m):
        print(m, "is prime")
    #     if (c == 0):
    #         P = m -1
    #         the smallest k in a**k - 1 that is divisible my m, should be k = m -1
