from math import *

def linear_equation_solver(linear_coefficient, constant):
    if linear_coefficient == 0:
        return None
    return -constant / linear_coefficient,


def quadratic_equation_solver(quadratic_coefficient, linear_coefficient, constant):
    discriminant = linear_coefficient / quadratic_coefficient * linear_coefficient / quadratic_coefficient / 4 - constant / quadratic_coefficient
    if discriminant < 0:
        return None,
    elif discriminant == 0:
        return -linear_coefficient / quadratic_coefficient / 2,
    else:
        return -linear_coefficient / quadratic_coefficient / 2 + sqrt(discriminant), -linear_coefficient / quadratic_coefficient / 2 - sqrt(discriminant)


def equation_solver(quadratic_coefficient, linear_coefficient, constant):
    if quadratic_coefficient == 0:
        return linear_equation_solver(linear_coefficient, constant)
    else:
        return quadratic_equation_solver(quadratic_coefficient, linear_coefficient, constant)
