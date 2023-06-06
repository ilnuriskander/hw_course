# Напишите 5 тестов на функцию all_division. Обязательно должен быть тест деления на ноль.
# Промаркируйте часть тестов. Например, smoke.
# В консоли с помощью pytest сделайте вызов:
# 1) Всех тестов
# 2) Только с маркером smoke
# 3) По маске. Выберите такую маску, чтобы под неё подпадали не все тесты, но больше одного
# Пришлите на проверку файл с тестами и скрины с вызовами и их результаты

import pytest

def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.smoke
def test_1():
    assert all_division(3, 2, 1) == 1.5


@pytest.mark.smoke
def test_minus():
    assert all_division(5, -2, 2) == -1.25

@pytest.mark.acceptance
def test_1_argument():
    assert all_division(3) == 3

@pytest.mark.acceptance
def test_zero():
    with pytest.raises(ZeroDivisionError):
        all_division(2, 0)

@pytest.mark.acceptance
def test_str():
    with pytest.raises(TypeError):
        all_division(2, '3')


