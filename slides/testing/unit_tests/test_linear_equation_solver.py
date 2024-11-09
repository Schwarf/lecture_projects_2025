import pytest

from testing.unit_test_production_code import linear_equation_solver


# Test for a positive solution
def test_linear_equation_solver_with_positive_coefficient_and_constant():
    # Arrange
    linear_coefficient = 2
    constant = -10
    expected_result = 5
    # Act
    result = linear_equation_solver(linear_coefficient, constant)
    # Assert
    assert result == expected_result


# Test for a negative solution
def test_linear_equation_solver_with_negative_coefficient_and_positive_constant():
    # Arrange
    linear_coefficient = -4
    constant = 8
    expected_result = 2
    # Act
    result = linear_equation_solver(linear_coefficient, constant)
    # Assert
    assert result == expected_result


# Test for zero constant, should return 0 regardless of coefficient
def test_linear_equation_solver_with_zero_constant_returns_zero():
    # Arrange
    linear_coefficient = 5
    constant = 0
    expected_result = 0
    # Act
    result = linear_equation_solver(linear_coefficient, constant)
    # Assert
    assert result == expected_result


# Test for non-integer solution
def test_linear_equation_solver_with_non_integer_solution():
    # Arrange
    linear_coefficient = 3
    constant = -7
    expected_result = 7 / 3
    # Act
    result = linear_equation_solver(linear_coefficient, constant)
    # Assert
    assert result == pytest.approx(expected_result)


# Test for when linear_coefficient is zero
def test_linear_equation_solver_with_zero_coefficient_returns_none():
    # Arrange
    linear_coefficient = 0
    constant = 5
    expected_result = None
    # Act
    result = linear_equation_solver(linear_coefficient, constant)
    # Assert
    assert result == expected_result


# Test for when both coefficients are zero
def test_linear_equation_solver_with_both_coefficients_zero_return_none():
    # Arrange
    linear_coefficient = 0
    constant = 0
    expected_result = None
    # Act
    result = linear_equation_solver(linear_coefficient, constant)
    # Assert
    assert result == expected_result
