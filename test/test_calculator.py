import pytest
from calculator import Calculator

@pytest.fixture(autouse=True)
def clear_history():
    """Fixture to clear history before each test."""
    Calculator.clear_history()

def test_add():
    assert Calculator.add(2, 3) == 5

def test_subtract():
    assert Calculator.subtract(5, 3) == 2

def test_multiply():
    assert Calculator.multiply(3, 4) == 12

def test_divide():
    assert Calculator.divide(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        Calculator.divide(5, 0)

def test_last_calculation():
    Calculator.add(1, 1)
    last_calc = Calculator.get_last_calculation()
    assert last_calc.operation == "add"
    assert last_calc.operands == (1, 1)
    assert last_calc.result == 2

def test_history():
    Calculator.add(3, 4)
    Calculator.multiply(2, 5)
    assert len(Calculator.history) == 2
