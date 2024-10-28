from math import *


def quadratic_equation_solver(quadratic_coefficient, linear_coefficient, constant):
    if quadratic_coefficient == 0:
        if linear_coefficient == 0:
            return None
        return -constant / linear_coefficient,

    discriminant = linear_coefficient / quadratic_coefficient * linear_coefficient / quadratic_coefficient / 4 - constant / quadratic_coefficient
    if discriminant < 0:
        return None,
    elif discriminant == 0:
        return -linear_coefficient / quadratic_coefficient / 2,
    else:
        return -linear_coefficient / quadratic_coefficient / 2 + sqrt(discriminant), -linear_coefficient / quadratic_coefficient / 2 - sqrt(discriminant)
