from typing import Union

class Calculator:
    """A simple calculator class that provides basic arithmetic operations."""

    @staticmethod
    def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """Add two numbers.
        
        Args:
            a: First number
            b: Second number
        
        Returns:
            The sum of a and b
        """
        return a + b

    @staticmethod
    def subtract(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """Subtract two numbers.
        
        Args:
            a: First number
            b: Second number to subtract from first
        
        Returns:
            The difference between a and b
        """
        return a - b

    @staticmethod
    def multiply(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """Multiply two numbers.
        
        Args:
            a: First number
            b: Second number
        
        Returns:
            The product of a and b
        """
        return a * b

    @staticmethod
    def divide(a: Union[int, float], b: Union[int, float]) -> float:
        """Divide two numbers.
        
        Args:
            a: Numerator
            b: Denominator
        
        Raises:
            ZeroDivisionError: If b is zero
        
        Returns:
            The quotient of a divided by b
        """
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b

