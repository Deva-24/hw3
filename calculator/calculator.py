"""
This module implements a simple calculator that can perform basic arithmetic operations
and keep track of calculation history.
"""

from typing import List, Tuple, Optional

class Calculation:
    """Class to represent a calculation and its result."""

    def __init__(self, operation: str, operands: Tuple[float, float], result: float):
        self.operation = operation
        self.operands = operands
        self.result = result

    def __str__(self):
        return f"{self.operands[0]} {self.operation} {self.operands[1]} = {self.result}"

class Calculator:
    """A simple calculator that supports addition, subtraction, multiplication, and division, 
    while keeping a history of calculations.
    """
    
    history: List[Calculation] = []

    @staticmethod
    def add(a: float, b: float) -> float:
        """Return the sum of a and b, and add this calculation to history."""
        result = a + b
        Calculator._add_to_history("add", (a, b), result)
        return result

    @staticmethod
    def subtract(a: float, b: float) -> float:
        """Return the difference of a and b, and add this calculation to history."""
        result = a - b
        Calculator._add_to_history("subtract", (a, b), result)
        return result

    @staticmethod
    def multiply(a: float, b: float) -> float:
        """Return the product of a and b, and add this calculation to history."""
        result = a * b
        Calculator._add_to_history("multiply", (a, b), result)
        return result

    @staticmethod
    def divide(a: float, b: float) -> float:
        """Return the quotient of a and b, and add this calculation to history.
        
        Raises:
            ZeroDivisionError: If b is zero.
        """
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        result = a / b
        Calculator._add_to_history("divide", (a, b), result)
        return result

    @classmethod
    def get_last_calculation(cls) -> Optional[Calculation]:
        """Return the last calculation from the history, or None if the history is empty."""
        return cls.history[-1] if cls.history else None

    @classmethod
    def _add_to_history(cls, operation: str, operands: Tuple[float, float], result: float) -> None:
        """Add a calculation to the history."""
        cls.history.append(Calculation(operation, operands, result))

    @classmethod
    def clear_history(cls) -> None:
        """Clear the calculation history."""
        cls.history.clear()
