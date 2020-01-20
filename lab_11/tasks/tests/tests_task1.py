import pytest

from lab_11.tasks.tools.calculator import (
    Calculator,
    CalculatorError,
    EmptyMemory,
    NotNumberArgument,
    WrongOperation,
)


@pytest.fixture
def calculator():
    calculator = Calculator()
    return calculator


@pytest.mark.parametrize(
    ('op', 'arg1', 'arg2', 'res'),
    [
        ('+', 1, 2, 3),
        ('-', 4, 2, 2),
        ('*', 10, 4, 40),
        ('/', 6, 3, 2)
    ]
)
def test_run(calculator, op, arg1, arg2, res):
    assert calculator.run(op, arg1, arg2) == res


def test_memorize(calculator):
    calculator.run('-', 6, 4)
    calculator.memorize()
    assert calculator.memory == 2
    assert calculator.run('+', 2) == 4


def test_wrong_operation(calculator):
    with pytest.raises(WrongOperation):
        calculator.run('x', 4, 5)


def test_not_number_argument(calculator):
    with pytest.raises(NotNumberArgument):
        calculator.run('+', 4, 'b')
    with pytest.raises(NotNumberArgument):
        calculator.run('+', 'b', 4)


def test_not_number_argument_list(calculator):
    with pytest.raises(NotNumberArgument):
        calculator.run('+', 4, [1, 2, 3])


def test_calculator_error(calculator):
    with pytest.raises(CalculatorError):
        calculator.run('/', 9, 0)


def test_empty_in_memory(calculator):
    with pytest.raises(EmptyMemory):
        calculator.in_memory()


def test_empty_memory(calculator):
    with pytest.raises(EmptyMemory):
        calculator.run('/', 9)
