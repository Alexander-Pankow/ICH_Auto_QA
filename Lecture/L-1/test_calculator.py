import pytest

from calculator import  Calculator

@pytest.fixture
def calculator():
    return Calculator()

@pytest.mark.positive
def test_sum_positive(calculator):
    res = calculator.sum(1, 2)
    assert res == 3

def test_sum_negative(calculator):
    #calculator = Calculator()    комментируем из за строки 5-7 теперь не нужно везде писать
    res = calculator.sum(-1, -4)
    assert res == -5

@pytest.mark.positive
def test_sum_positive_negative(calculator):
    #calculator = Calculator()
    res = calculator.sum(5, -2)
    assert res == 3

def test_sum_negative_positive(calculator):
    #calculator = Calculator()
    res = calculator.sum(-1, 5)
    assert res == 4