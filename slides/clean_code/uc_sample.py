from math import sqrt


def compute(a1, a2, a3):
    if a1 == 0:
        if a2 == 0:
            return None
        return -a3 / a2,

    a4 = a2 / a1 * a2 / a1 / 4 - a3 / a1
    if a4 < 0:
        return None,
    elif a4 == 0:
        return -a2 / a1 / 2,
    else:
        return -a2 / a1 / 2 + sqrt(a4), -a2 / a1 / 2 - sqrt(a4)
