class Calculator:
    @staticmethod
    def add(a: float, b: float) -> float:
        return a + b

    @staticmethod
    def subtract(a: float, b: float) -> float:
        return a - b

    @staticmethod
    def multiply(a: float, b: float) -> float:
        return a * b

    @staticmethod
    def divide(a: float, b: float) -> float:
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b



class Calculation:
    def __init__(self, operation: str, operands: tuple[float, float], result: float):
        self.operation = operation
        self.operands = operands
        self.result = result

    def __str__(self):
        return f"{self.operands[0]} {self.operation} {self.operands[1]} = {self.result}"

class Calculator:
    history: list[Calculation] = []

    @staticmethod
    def add(a: float, b: float) -> float:
        result = a + b
        Calculator._add_to_history("add", (a, b), result)
        return result

    @staticmethod
    def subtract(a: float, b: float) -> float:
        result = a - b
        Calculator._add_to_history("subtract", (a, b), result)
        return result

    @staticmethod
    def multiply(a: float, b: float) -> float:
        result = a * b
        Calculator._add_to_history("multiply", (a, b), result)
        return result

    @staticmethod
    def divide(a: float, b: float) -> float:
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        result = a / b
        Calculator._add_to_history("divide", (a, b), result)
        return result

    @classmethod
    def get_last_calculation(cls) -> Calculation:
        return cls.history[-1] if cls.history else None

    @classmethod
    def _add_to_history(cls, operation: str, operands: tuple[float, float], result: float) -> None:
        cls.history.append(Calculation(operation, operands, result))

    @classmethod
    def clear_history(cls) -> None:
        cls.history.clear()
