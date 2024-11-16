import pytest
from unittest.mock import patch, MagicMock
from integration_tests.src.rlc_circuit_analyzer import RLCCircuitAnalyzer

# Test data for different cases
test_data = [
    # Case 1: No real roots (overdamped circuit)
    {"resistance": 100, "inductance": 1e-3, "capacitance": 1e-6, "expected": None},

    # Case 2: One real root (critically damped circuit)
    {"resistance": 50, "inductance": 1e-3, "capacitance": 1e-6, "expected": 5000},

    # Case 3: Two real roots (underdamped circuit)
    {"resistance": 10, "inductance": 1e-3, "capacitance": 1e-6, "expected": (3000, 7000)},
]

@pytest.mark.parametrize("data", test_data)
@patch("integration_tests.src.equation_solverEquationSolver")
def test_analyze_resonance(mock_solver_class, data):
    # Create the RLCCircuitAnalyzer instance
    analyzer = RLCCircuitAnalyzer(data["resistance"], data["inductance"], data["capacitance"])

    # Set up the mock for EquationSolver to return the expected value
    mock_solver_instance = MagicMock()
    mock_solver_instance.solve.return_value = data["expected"]
    mock_solver_class.return_value = mock_solver_instance

    # Call the analyze_resonance method
    result = analyzer.analyze_resonance()

    # Assert that the result matches the expected value
    assert result == data["expected"], f"Expected {data['expected']} but got {result}"

    # Assert that EquationSolver was initialized with the correct coefficients
    a = data["inductance"] * data["capacitance"]
    b = data["resistance"]
    c = 1
    mock_solver_class.assert_called_once_with(a, b, c)

    # Assert that the solve method was called on the mock instance
    mock_solver_instance.solve.assert_called_once()
