import random
from numba import njit
from typing import *
import numpy as np


@njit
def generate(a1, m1, a2, m2, limit):
    """for k=2, c=0"""
    R = np.empty(limit)

    y1 = random.randint(1, m1 - 1)
    y2 = random.randint(1, m2 - 1)

    for i in range(limit):
        y1 = a1 * y1 % m1
        y2 = a2 * y2 % m2

        x = (y1 - y2) % m1

        if x > 0:
            R[i] = x / m1
        elif x < 0:
            R[i] = (x / m1) + 1
        elif x == 0:
            R[i] = m1 / m2

    return R
