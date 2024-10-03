import pytest
from calculator.calculator import Calculator

@pytest.fixture(autouse=True)
def clear_history():
    """Fixture to clear history before each test."""
    Calculator.clear_history()

def test_add():
    """Test the addition functionality of the Calculator."""
    assert Calculator.add(2, 3) == 5

def test_subtract():
    """Test the subtraction functionality of the Calculator."""
    assert Calculator.subtract(5, 3) == 2

def test_multiply():
    """Test the multiplication functionality of the Calculator."""
    assert Calculator.multiply(3, 4) == 12

def test_divide():
    """Test the division functionality of the Calculator."""
    assert Calculator.divide(10, 2) == 5

def test_divide_by_zero():
    """Test that division by zero raises a ZeroDivisionError."""
    with pytest.raises(ZeroDivisionError):
        Calculator.divide(5, 0)

def test_last_calculation():
    """Test that the last calculation is stored correctly."""
    Calculator.add(1, 1)
    last_calc = Calculator.get_last_calculation()
    assert last_calc.operation == "add"
    assert last_calc.operands == (1, 1)
    assert last_calc.result == 2

def test_history():
    """Test that the Calculator stores calculation history."""
    Calculator.add(3, 4)
    Calculator.multiply(2, 5)
    assert len(Calculator.history) == 2
