import pytest
import datetime
import time

dt = datetime.datetime.now()


@pytest.fixture(scope='class', autouse=True)
def s_time():
    start_time = dt.strftime('%d.%m %H:%M:%S')
    yield print(start_time)
    print(dt.strftime('%d.%m %H:%M:%S'))
#


@pytest.fixture()
def func_time():
    start = time.time()
    yield
    end = time.time()
    print(end - start)




