from math import *
from typing import Tuple, Union


class RCCircuitEquationSolver:

    def __init__(self, quadratic_coefficient: float, linear_coefficient: float, constant: float):
        self._quadratic_coefficient = quadratic_coefficient
        self._linear_coefficient = linear_coefficient
        self._constant = constant

    def solve_linear_equation(self) -> Union[None, float]:
        if self._linear_coefficient == 0:
            return None
        return -self._constant / self._linear_coefficient

    def solve_quadratic_equation(self) -> Union[None, float, Tuple[float, float]]:
        discriminant = self._linear_coefficient / self._quadratic_coefficient * self._linear_coefficient / self._quadratic_coefficient / 4 - self._constant / self._quadratic_coefficient
        if discriminant < 0:
            return None
        elif discriminant == 0:
            return -self._linear_coefficient / self._quadratic_coefficient / 2
        else:
            solution1 = -self._linear_coefficient / self._quadratic_coefficient / 2 + sqrt(discriminant)
            solution2 = -self._linear_coefficient / self._quadratic_coefficient / 2 - sqrt(discriminant)
            return solution1, solution2

    def solve(self) -> Union[None, float, Tuple[float, float]]:
        if self._quadratic_coefficient == 0:
            return self.solve_linear_equation()
        else:
            return self.solve_quadratic_equation()
