from Framework.distributions import *


def directTransform(R, R2, dist):
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


class RandomVariateGenerator:
    def __init__(self, random_numbers: List[float]):
        self.random_numbers = random_numbers

    def Normal(self, *distArgs) -> List[float]:
        dist = NormalDist(*distArgs)
        return directTransform(self.random_numbers[0], self.random_numbers[1], dist)

    def Uniform(self, *distArgs) -> List[float]:
        dist = UniformDist(*distArgs)
        X = [dist.min + (dist.max - dist.min) * r for r in self.random_numbers]
        return X

    # ======================================
    #            Extra Generators
    # ======================================

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
