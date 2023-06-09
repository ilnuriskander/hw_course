# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.

import pytest


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division

class Test:
    def test_1(self):
        assert all_division(3, 2, 1) == 1.5


    def test_minus(self, func_time):
        assert all_division(5, -2, 2) == -1.25


    def test_1_argument(self):
        assert all_division(3) == 3


    def test_zero(self):
        with pytest.raises(ZeroDivisionError):
            all_division(2, 0)


    def test_str(self):
        with pytest.raises(TypeError):
            all_division(2, '3')
