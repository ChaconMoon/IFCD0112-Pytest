import pytest

def test_suma_tres_cinco():
    resultado = 3 + 5
    assert resultado == 8

def test_resta_diez_cinco():
    resultado = 10 - 5
    assert resultado == 5

def test_dividir_diez_cero():
    with pytest.raises(ZeroDivisionError):
        resultado = 10 / 0