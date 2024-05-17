from typing import *
import math


class NormalDist:
    def __init__(self, mean, stddev):
        self.mean = mean
        self.stddev = stddev

    def pdf(self, x):
        return (1 / (self.stddev * math.sqrt(2 * math.pi))) * math.e ** (
            (-1 / 2) * ((x - self.mean) / self.stddev) ** 2
        )


class UniformDist:
    def __init__(self, min, max):
        self.min = min
        self.max = max

    def pdf(self):
        return 1 / (max - min)

    def cdf(self, X):
        return (X - min) / (max - min)


# print(generateUniform(UniformDist(3, 8), [0.23, 0.75, 0.44, 0.34, 0.91]))


class ExponentialDist:
    def __init__(self, lambdaa):
        self.lambdaa = lambdaa

    def pdf(self, x):
        return self.lambdaa * math.e ** (-1 * self.lambdaa * x)

    def cdf(self, x):
        # for x >= 0
        return 1 - math.e ** (-1 * self.lambdaa * x)


class WeibullDist:
    def __init__(self, alpha, beta):
        self.alpha = alpha
        self.beta = beta

    def pdf(self, x):
        if x == 0:
            return 0
        return (
            (self.beta / (self.alpha**self.beta))
            * (x ** (self.beta - 1))
            * (math.e ** (-1 * (x / self.alpha) ** self.beta))
        )


class ChiSquareDist:
    def __init__(self, k):
        self.k = k


class TriangularDist:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def pdf(self, x):
        if x >= 0 and x <= 1:
            return x
        if x >= 1 and x <= 2:
            return 2 - x
        return 0

    def cdf(self, x):
        if x <= 0:
            return 0
        if x > 0 and x <= 1:
            return x**2 / 2
        if x > 1 and x <= 2:
            return 1 - (2 - x) ** 2 / 2
        if x > 2:
            return 1


class ErlangDist:
    def __init__(self, k, theta):
        self.k = k
        self.theta = theta


class PoissonDist:
    def __init__(self, alpha):
        self.alpha = alpha

    def pdf(self, n):
        ((math.e ** (-1 * self.alpha)) * (self.alpha**n)) / math.factorial(n)
