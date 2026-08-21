import pytest
from use_cases import suma

def test_suma_correct():
    assert suma(3, 5) == 8

def test_suma_value_error():
    with pytest.raises(ValueError):
        suma("NaN", 5)

def test_suma_type_error():
    with pytest.raises(TypeError):
        suma(None, 5)

def test_suma_overflow_error():
    with pytest.raises(OverflowError):
        suma(float('inf'), 5)
