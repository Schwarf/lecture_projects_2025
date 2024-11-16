from typing import Tuple, Union
from integration_tests.src.equation_solver import EquationSolver

class RLCCircuitAnalyzer:
    def __init__(self, resistance: float, inductance: float, capacitance: float):
        self.resistance = resistance
        self.inductance = inductance
        self.capacitance = capacitance

    def analyze_resonance(self) -> Union[None, float, Tuple[float, float]]:
        # Define the coefficients for the quadratic equation: a * ω^2 + b * ω + c = 0
        a = self.inductance * self.capacitance
        b = self.resistance
        c = 1

        # Initialize the solver with the coefficients
        solver = EquationSolver(a, b, c)

        # Solve for resonant frequencies
        return solver.solve()

