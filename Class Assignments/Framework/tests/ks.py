import math
from numba import njit
from typing import *


@njit
def test(R: List[float], D_alpha: float) -> bool:
    """Kolmogorov-Smirnov Test
    args:
        R: numbers
        D_alpha: alpha for specified signifcance level
    """

    N = len(R)
    D = 0

    # seems to be faster than np.sort()
    R.sort()

    for i in range(N):
        # in this math formula, i starts from 1
        D_plus_i = (i + 1) / N - R[i]
        D_minus_i = R[i] - i / N
        if D_plus_i > D:
            D = D_plus_i
        if D_minus_i > D:
            D = D_minus_i

    return D <= D_alpha


def isUniform(R: List[float], alpha: float) -> bool:
    # because we can't call this function when using njit
    D_alpha = getKSCriticalValue(len(R), alpha)
    return test(R, D_alpha)


# [a = 0.10, a = 0.05, a = 0.01]
KS_CRITICAL_VALUES = [
    [0.950, 0.975, 0.995],
    [0.776, 0.842, 0.929],
    [0.642, 0.708, 0.828],
    [0.564, 0.624, 0.733],
    [0.510, 0.565, 0.669],
    [0.470, 0.521, 0.618],
    [0.438, 0.486, 0.577],
    [0.411, 0.457, 0.543],
    [0.388, 0.432, 0.514],
    [0.368, 0.410, 0.490],
    [0.352, 0.391, 0.468],
    [0.338, 0.375, 0.450],
    [0.325, 0.361, 0.433],
    [0.314, 0.349, 0.418],
    [0.304, 0.338, 0.404],
    [0.295, 0.328, 0.392],
    [0.286, 0.318, 0.381],
    [0.278, 0.309, 0.371],
    [0.272, 0.301, 0.363],
    [0.264, 0.294, 0.356],  # 20
    None,
    None,
    None,
    None,
    [0.24, 0.27, 0.32],  # 25
    None,
    None,
    None,
    None,
    [0.22, 0.24, 0.29],  # 30
    None,
    None,
    None,
    None,
    [0.21, 0.23, 0.27],  # 35
]


def getKSCriticalValue(N: int, alpha: float) -> float:
    if N > 35:
        if alpha == 0.1:
            return 1.22 / math.sqrt(N)
        if alpha == 0.05:
            return 1.36 / math.sqrt(N)
        if alpha == 0.01:
            return 1.63 / math.sqrt(N)
    if alpha == 0.1:
        return KS_CRITICAL_VALUES[N - 1][0]
    if alpha == 0.05:
        return KS_CRITICAL_VALUES[N - 1][1]
    if alpha == 0.01:
        return KS_CRITICAL_VALUES[N - 1][2]
