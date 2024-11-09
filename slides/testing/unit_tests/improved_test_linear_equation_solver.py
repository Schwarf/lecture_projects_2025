import pytest
from math import sqrt, log, sin, cos, pi
from testing.production_code import linear_equation_solver

# Test for when the coefficient is zero
@pytest.mark.parametrize(
    "linear_coefficient, constant, expected_result",
    [
        (0, 5, None),
        (0, -5, None),
        (0, 0, None),
        (0, 100, None),
        (0, -100, None)
    ]
)
def test_linear_equation_solver_zero_coefficient(linear_coefficient, constant, expected_result):
    result = linear_equation_solver(linear_coefficient, constant)
    assert result == expected_result

# Test for positive solution
@pytest.mark.parametrize(
    "linear_coefficient, constant, expected_result",
    [
        (2, -10, 5),
        (0.5, -1, 2),
        (-1, 3, 3),
        (4, -20, 5),
        (-10, 60, 6)
    ]
)
def test_linear_equation_solver_positive_solution(linear_coefficient, constant, expected_result):
    result = linear_equation_solver(linear_coefficient, constant)
    assert result == expected_result

# Test for negative solution
@pytest.mark.parametrize(
    "linear_coefficient, constant, expected_result",
    [
        (-4, 8, 2),
        (-2, 4, 2),
        (-0.5, 1, 2),
        (-1, 3, 3.0),
        (-10, 50, 5.0)
    ]
)
def test_linear_equation_solver_negative_solution(linear_coefficient, constant, expected_result):
    result = linear_equation_solver(linear_coefficient, constant)
    assert result == expected_result

# Test for zero constant
@pytest.mark.parametrize(
    "linear_coefficient, constant, expected_result",
    [
        (5, 0, 0),
        (-5, 0, 0),
        (0.5, 0, 0),
        (-0.5, 0, 0),
        (10, 0, 0)
    ]
)
def test_linear_equation_solver_zero_constant(linear_coefficient, constant, expected_result):
    result = linear_equation_solver(linear_coefficient, constant)
    assert result == expected_result

# Test for non-integer solution
@pytest.mark.parametrize(
    "linear_coefficient, constant, expected_result",
    [
        (3, -7, pytest.approx(7 / 3)),
        (2.5, -5, pytest.approx(2)),
        (1.5, -3, pytest.approx(2)),
        (7, -14.5, pytest.approx(2.0714285714)),
        (10, -3, pytest.approx(0.3))
    ]
)
def test_linear_equation_solver_non_integer_solution(linear_coefficient, constant, expected_result):
    result = linear_equation_solver(linear_coefficient, constant)
    assert result == expected_result

# Test for general float inputs
@pytest.mark.parametrize(
    "linear_coefficient, constant, expected_result",
    [
        (1.2, -6.6, pytest.approx(5.5)),
        (-2.8, 8.4, pytest.approx(3.0)),
        (3.3, -6.6, pytest.approx(2.0)),
        (10.5, -21, pytest.approx(2.0)),
        (0.75, -1.5, pytest.approx(2.0)),
        (sqrt(0.75), sin(-0.51), pytest.approx(sin(0.51)/sqrt(0.75))),
        (log(7509210.13131), cos(0.8888), pytest.approx(-cos(0.8888)/log(7509210.13131)))
    ]
)
def test_linear_equation_solver_float_inputs(linear_coefficient, constant, expected_result):
    result = linear_equation_solver(linear_coefficient, constant)
    assert result == expected_result
