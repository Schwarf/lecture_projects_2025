from math import *
from typing import Tuple, Union


def linear_equation_solver(linear_coefficient: float, constant: float) -> Union[None, float]:
    if linear_coefficient == 0:
        return None
    return -constant / linear_coefficient


def quadratic_equation_solver(quadratic_coefficient: float, linear_coefficient: float, constant: float) -> Union[None, float, Tuple[float, float]]:
    discriminant = linear_coefficient / quadratic_coefficient * linear_coefficient / quadratic_coefficient / 4 - constant / quadratic_coefficient
    if discriminant < 0:
        return None
    elif discriminant == 0:
        return -linear_coefficient / quadratic_coefficient / 2
    else:
        solution1 = -linear_coefficient / quadratic_coefficient / 2 + sqrt(discriminant)
        solution2 = -linear_coefficient / quadratic_coefficient / 2 - sqrt(discriminant)
        return solution1, solution2


def equation_solver(quadratic_coefficient: float, linear_coefficient: float, constant: float) -> Union[None, float, Tuple[float, float]]:
    if quadratic_coefficient == 0:
        return linear_equation_solver(linear_coefficient, constant)
    else:
        return quadratic_equation_solver(quadratic_coefficient, linear_coefficient, constant)
