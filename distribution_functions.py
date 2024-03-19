import random


def uniform(min: float, max: float) -> float:
    return random.random() * (max - min) + min
