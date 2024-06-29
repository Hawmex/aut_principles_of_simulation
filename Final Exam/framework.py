import math
from typing import *

import matplotlib.pyplot as plt


class Rng:
    @staticmethod
    def lcg(seed: int, modulus: int, multiplier: int, increment=0, returnInts=False):
        randomInt = seed

        while True:
            yield randomInt if returnInts else randomInt / modulus

            randomInt = (multiplier * randomInt + increment) % modulus

    @staticmethod
    def clcg(seeds: List[int], moduli: List[int], multipliers: List[int]):
        generators = [
            Rng.lcg(seed, modulus, multiplier, returnInts=True)
            for seed, modulus, multiplier in zip(seeds, moduli, multipliers)
        ]

        modulus = max(moduli)

        while True:
            randomInts = [next(generator) for generator in generators]

            randomInt = sum(
                randomInt * (1 if i % 2 == 0 else -1)
                for i, randomInt in enumerate(randomInts)
            ) % (modulus - 1)

            yield randomInt / modulus if randomInt > 0 else (modulus - 1) / modulus


class Utils:
    @staticmethod
    def getCycle(generator: Generator[float, Any, NoReturn]):
        cycle: List[float] = []

        while (randomValue := next(generator)) not in cycle:
            cycle.append(randomValue)

        return cycle

    @staticmethod
    def plotNums(nums: List[float | int], bins: int | None = None):
        if bins is None:
            bins = int(math.sqrt(len(nums)))

        plt.figure()
        plt.hist(nums, bins)
        plt.show()


class Tests:
    @staticmethod
    def ks(nums: List[float | int]):
        nums = sorted(nums)
        n = len(nums)

        D_plus = max((i + 1) / n - num for i, num in enumerate(nums))
        D_minus = max(num - i / n for i, num in enumerate(nums))

        D = max(D_plus, D_minus)

        return D

    @staticmethod
    def chiSq(observed: List[float | int], expected: List[float | int]):
        return sum((o - e) ** 2 / e for o, e in zip(observed, expected))

    @staticmethod
    def autoCorr(nums: List[float | int], start: int, lag: int):
        pairs = (len(nums) - (start + 1)) // lag - 1

        nominator = (
            sum(
                nums[start + k * lag] * nums[start + (k + 1) * lag]
                for k in range(pairs + 1)
            )
            / (pairs + 1)
            - 0.25
        )

        denominator = math.sqrt(13 * pairs + 7) / (12 * (pairs + 1))

        return nominator / denominator


class RandomVariate:
    generator = Rng.lcg(seed=123_457, modulus=2**31 - 1, multiplier=7**5)

    @staticmethod
    def uniform(low: float, high: float):
        randomValue = next(RandomVariate.generator)

        return (high - low) * randomValue + low

    @staticmethod
    def exponential(mean: float):
        randomValue = next(RandomVariate.generator)

        return -mean * math.log(randomValue)

    @staticmethod
    def weibull(alpha: float, beta: float):
        randomValue = next(RandomVariate.generator)

        return alpha * (-math.log(randomValue)) ** (1 / beta)

    @staticmethod
    def triangular(low: float, mode: float, high: float):
        randomValue = next(RandomVariate.generator)

        if randomValue <= (mode - low) / (high - low):
            return math.sqrt((high - low) * (mode - low) * randomValue) + low
        else:
            return high - math.sqrt((high - low) * (high - mode) * (1 - randomValue))

    @staticmethod
    def normal(mean: float, std: float):
        randomValue1 = next(RandomVariate.generator)
        randomValue2 = next(RandomVariate.generator)

        radius = math.sqrt(-2 * math.log(randomValue1))
        theta = 2 * math.pi * randomValue2

        randomVariate1 = radius * math.cos(theta)
        randomVariate2 = radius * math.sin(theta)

        randomVariate1 = std * randomVariate1 + mean
        randomVariate2 = std * randomVariate2 + mean

        return randomVariate1 if next(RandomVariate.generator) < 0.5 else randomVariate2

    @staticmethod
    def logNormal(mean: float, std: float):
        return math.exp(RandomVariate.normal(mean, std))

    @staticmethod
    def erlang(stages: int, mean: float):
        randomValues = [next(RandomVariate.generator) for _ in range(stages)]

        return -mean / stages * math.log(math.prod(randomValues))

    @staticmethod
    def poisson(mean: int):
        if mean >= 15:
            z = RandomVariate.normal(0, 1)

            return math.ceil(math.sqrt(mean) * z + mean - 0.5)

        n = 0
        p = 1

        while (p := p * next(RandomVariate.generator)) >= math.exp(-mean):
            n += 1

        return n

    @staticmethod
    def empirical(nums, frequencies):
        randomValue = next(RandomVariate.generator)
        total = sum(frequencies)

        index = -1
        cumulativeFrequency = 0

        for frequency in frequencies:
            relativeFrequency = frequency / total
            if cumulativeFrequency + relativeFrequency <= randomValue:
                cumulativeFrequency += relativeFrequency
                index += 1
            else:
                break

        x0 = nums[index]
        x1 = nums[index + 1]
        relativeFrequency = frequencies[index + 1] / total

        return x0 + (x1 - x0) / relativeFrequency * (randomValue - cumulativeFrequency)

    @staticmethod
    def discreteUniform(low: int, high: int):
        k = high - low + 1
        randomValue = next(RandomVariate.generator)

        return math.floor(k * randomValue) + low

    @staticmethod
    def nspp(times, means):
        minMean = min(means)
        currentMeanIndex = 0
        t = 0

        while True:
            t += RandomVariate.exponential(minMean)

            if t >= times[currentMeanIndex + 1]:
                currentMeanIndex += 1

            randomValue = next(RandomVariate.generator)

            if randomValue <= minMean / means[currentMeanIndex]:
                yield t


class SimEvent[T: SimController]:
    def __init__(self, interval: float) -> None:
        self.dueTime: float
        self.controller: T

        self.interval = interval

    def trigger(self) -> None:
        raise NotImplementedError()


class SimController:
    def __init__(self, stopTime: float, initialEvent: SimEvent | None = None) -> None:
        self.futureEvents: List[SimEvent] = []
        self.clock: float = 0

        self.stopTime = stopTime

        if initialEvent is not None:
            self.dispatchEvent(initialEvent)

    def dispatchEvent(self, event: SimEvent) -> None:
        event.dueTime = self.clock + event.interval
        event.controller = self

        self.futureEvents.append(event)
        self.futureEvents.sort(key=lambda event: event.dueTime)

    def simulate(self) -> None:
        while self.futureEvents[0].dueTime <= self.stopTime:
            upcomingEvent = self.futureEvents.pop(0)
            self.clock = upcomingEvent.dueTime

            upcomingEvent.trigger()
