from typing import *
from distributions import *
from helpers import *
import random
from numba import njit
import numpy as np


@njit
def lcm(seed, a, c, m, limit):
    R = np.empty(limit)
    x = seed
    for i in range(limit):
        x = (x * a + c) % m
        R[i] = x / m
    return R


class CLCG:
    def __init__(self, k):
        self.k = k

    def generate(self, a1, m1, a2, m2):
        x01 = random.randint(1, m1)
        x02 = random.randint(2, m2)
        X1 = LCM(x01, a1, 0, m1).generate()
        X2 = LCM(x02, a2, 0, m2).generate()

        return [X1, X2]


# def LCM(x0: int, a: int, c: int, m: int) -> List[int]:


class LCM:
    # c = 0: multiplicative,
    # c != 0: mixed
    @staticmethod
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

    @staticmethod
    def generate(seed, a, c, m, limit=None):
        if limit is None:
            limit = m
        return lcm(seed, a, c, m, m)


class RandomNumberGenerator:
    @staticmethod
    def CLCG():
        """Combined Linear Congruential Generators"""
        pass

    @staticmethod
    def Streams():
        """Random-Number Streams"""
        pass

    # tozi yeknavakht, 0, 1


class RandomVariateGenerator:
    def __init__(self, random_numbers: List[float]):
        self.random_numbers = random_numbers

    def Weibull(self, *distArgs) -> List[float]:
        dist = WeibullDist(*distArgs)
        X = [
            dist.alpha * (-1 * math.log(1 - r)) ** (1 / dist.beta)
            for r in self.random_numbers
        ]
        return X

    def Exponential(self, *distArgs) -> List[float]:
        dist = ExponentialDist(*distArgs)
        X = [-1 * (1 / dist.lambdaa) * math.log(1 - r) for r in self.random_numbers]
        return X

    def Uniform(self, *distArgs) -> List[float]:
        dist = UniformDist(*distArgs)
        X = [dist.min + (dist.max - dist.min) * r for r in self.random_numbers]
        return X

    def Triangular(self, *distArgs) -> List[float]:
        # dist = TriangularDist(*distArgs)
        X = [
            (
                math.sqrt(2 * r)
                if (r >= 0 and r <= 1 / 2)
                else 2 - math.sqrt(2 * (1 - r))
            )
            for r in self.random_numbers
        ]
        return X

    def Normal():
        pass


def inverse_transform():
    # compute cdf F(x)
    # F(x) = R on range of X
    # X = F^-1(R)
    pass


def direct_transform(R, R2, dist):
    # z1 = b * math.cos(theta)
    Z1 = ((-2 * math.log(R)) ** (1 / 2)) * math.cos(2 * math.pi * R2)
    # z2 = b * math.sin(theta)
    Z2 = ((-2 * math.log(R)) ** (1 / 2)) * math.sin(2 * math.pi * R2)

    # X = [mu + sigma * Z for Z in [Z1, Z2]]
    X = [
        dist.mean + dist.stddev * Z1,
        dist.mean + dist.stddev * Z2,
    ]

    return X


# print(direct_transform(0.7, 0.87, NormalDist(14, 5)))


def convolution(dist, random_numbers):
    X = (-1 / (len(random_numbers) * dist.theta)) * math.log(math.prod(random_numbers))

    return X


def acceptance_rejection():
    pass


# print(convolution(ErlangDist(2, 5), [0.937, 0.217]))
