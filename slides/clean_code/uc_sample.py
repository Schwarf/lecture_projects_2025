from math import sqrt


def compute(a, b, c):
    if a == 0:
        if b == 0:
            return None
        return -c / b,

    p = b / a
    q = c / a
    d = p*p/4 - q
    if d < 0:
        return None,
    elif d == 0:
        return -p / 2,
    else:
        x1 = -p / 2 + sqrt(d)
        x2 = -p / 2 - sqrt(d)
        return x1, x2
