import pytest
from src.example.calculator import Calculator

def test_add():
    """Test the add method with various inputs."""
    assert Calculator.add(2, 3) == 5
    assert Calculator.add(-1, 1) == 0
    assert Calculator.add(0, 0) == 0
    assert Calculator.add(2.5, 3.5) == 6.0

def test_subtract():
    """Test the subtract method with various inputs."""
    assert Calculator.subtract(5, 3) == 2
    assert Calculator.subtract(1, 1) == 0
    assert Calculator.subtract(0, 5) == -5
    assert Calculator.subtract(3.5, 2.5) == 1.0

def test_multiply():
    """Test the multiply method with various inputs."""
    assert Calculator.multiply(2, 3) == 6
    assert Calculator.multiply(-2, 3) == -6
    assert Calculator.multiply(0, 5) == 0
    assert Calculator.multiply(2.5, 2) == 5.0

def test_divide():
    """Test the divide method with various inputs."""
    assert Calculator.divide(6, 2) == 3.0
    assert Calculator.divide(5, 2) == 2.5
    assert Calculator.divide(0, 5) == 0.0
    assert Calculator.divide(-6, 2) == -3.0

def test_divide_by_zero():
    """Test that division by zero raises an exception."""
    with pytest.raises(ZeroDivisionError):
        Calculator.divide(5, 0)

def test_type_hints():
    """Test that methods accept both integers and floats."""
    calc = Calculator()
    assert isinstance(calc.add(1, 2.0), float)
    assert isinstance(calc.subtract(1.0, 2), float)
    assert isinstance(calc.multiply(2, 2), int)
    assert isinstance(calc.divide(4, 2), float)

