from typing import Tuple, Union
from equation_solver import EquationSolver

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

# Example usage:
if __name__ == "__main__":
    # Example circuit values
    R = 100  # Resistance in ohms
    L = 1e-3  # Inductance in henries
    C = 10e-9  # Capacitance in farads

    analyzer = RLCCircuitAnalyzer(R, L, C)
    resonance_frequencies = analyzer.analyze_resonance()

    if resonance_frequencies is None:
        print("No real resonant frequency found.")
    elif isinstance(resonance_frequencies, tuple):
        print(f"Resonant Frequencies (ω): {resonance_frequencies[0]:.2e} rad/s, {resonance_frequencies[1]:.2e} rad/s")
    else:
        print(f"Resonant Frequency (ω): {resonance_frequencies:.2e} rad/s")
