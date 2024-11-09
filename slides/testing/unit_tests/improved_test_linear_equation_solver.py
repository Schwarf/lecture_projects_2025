import pytest
from math import sqrt, log, sin, cos, pi
from testing.production_code import linear_equation_solver

# Test for when the coefficient is zero
@pytest.mark.parametrize(
    "linear_coefficient, constant",
    [
        (0, 5),
        (0, -5),
        (0, 0),
        (0, 100),
        (0, -100)
    ]
)
def test_linear_equation_solver_zero_coefficient(linear_coefficient, constant):
    expected_result = None
    result = linear_equation_solver(linear_coefficient, constant)
    assert result == expected_result

# Test for positive solution
@pytest.mark.parametrize(
    "linear_coefficient, constant",
    [
        (2, -10),
        (0.5, -1),
        (-1, 3),
        (4, -20),
        (-10, 60)
    ]
)
def test_linear_equation_solver_positive_solution(linear_coefficient, constant):
    expected_result = -constant / linear_coefficient
    result = linear_equation_solver(linear_coefficient, constant)
    assert result == expected_result

# Test for negative solution
@pytest.mark.parametrize(
    "linear_coefficient, constant",
    [
        (-4, 8),
        (-2, 4),
        (-0.5, 1),
        (-1, 3),
        (-10, 50)
    ]
)
def test_linear_equation_solver_negative_solution(linear_coefficient, constant):
    expected_result = -constant / linear_coefficient
    result = linear_equation_solver(linear_coefficient, constant)
    assert result == expected_result

# Test for zero constant
@pytest.mark.parametrize(
    "linear_coefficient, constant",
    [
        (5, 0),
        (-5, 0),
        (0.5, 0),
        (-0.5, 0),
        (10, 0)
    ]
)
def test_linear_equation_solver_zero_constant(linear_coefficient, constant):
    expected_result = 0
    result = linear_equation_solver(linear_coefficient, constant)
    assert result == expected_result

# Test for non-integer solution
@pytest.mark.parametrize(
    "linear_coefficient, constant",
    [
        (3, -7),
        (2.5, -5),
        (1.5, -3),
        (7, -14.5),
        (10, -3)
    ]
)
def test_linear_equation_solver_non_integer_solution(linear_coefficient, constant):
    expected_result = -constant / linear_coefficient
    result = linear_equation_solver(linear_coefficient, constant)
    assert result == pytest.approx(expected_result)

# Test for general float inputs
@pytest.mark.parametrize(
    "linear_coefficient, constant",
    [
        (1.2, -6.6),
        (-2.8, 8.4),
        (3.3, -6.6),
        (10.5, -21),
        (0.75, -1.5),
        (sqrt(0.75), sin(-0.51)),
        (log(7509210.13131), cos(0.8888))
    ]
)
def test_linear_equation_solver_float_inputs(linear_coefficient, constant):
    expected_result = -constant / linear_coefficient
    result = linear_equation_solver(linear_coefficient, constant)
    assert result == pytest.approx(expected_result)
