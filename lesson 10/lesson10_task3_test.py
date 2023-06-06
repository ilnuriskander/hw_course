# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните

import pytest


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division

@pytest.mark.parametrize('a, b, c, result', [(3, 2, 1, 1.5), (5, -2, 2, -1.25), (90, 25, 2, 1.8)])
def test_1(a, b, c, result):
    all_division(a, b, c) == result

@pytest.mark.skip
@pytest.mark.parametrize('a, b, Exception', [(2, 0, Exception), (3, '4', Exception)])
def test2(a, b, Exception):
    with pytest.raises(Exception):
        all_division(a, b)

