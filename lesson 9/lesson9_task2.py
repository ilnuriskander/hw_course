# Напишите декоратор func_log, который может принимать аргумент file_log (Путь до файла), по умолчнию равен 'log.txt'
# Декоратор должен дозаписывать в файл имя вызываемой функции (можно получить по атрибуту __name__), дату и время вызова
# по формату:
# имя_функции вызвана %d.%m %H:%M:%S
# Для вывода времени нужно использовать модуль datetime и метод .strftime()
# https://pythonworld.ru/moduli/modul-datetime.html
# https://docs.python.org/3/library/datetime.html
# @func_log()
# def func1():
#     time.sleep(3)
# @func_log(file_log='func2.txt')
# def func2():
#     time.sleep(5)#
# Получим:
# в log.txt текст:
# func1 вызвана 30.05 14:12:42
# func1 вызвана 30.05 14:12:50
# в func2.txt текст:
# func2 вызвана 30.05 14:12:47

# Со звёздочкой. ДЕЛАТЬ НЕ ОБЯЗАТЕЛЬНО.
# help(func1) должен выводит одинаковый текст, когда есть декоратор на функции func1 и когда его нет
# Реализовать без подключения новых модулей и сторонних библиотек.

import datetime

dt = datetime.datetime.now()

def func_log(file_log):
    def write_logs(func):
        def wrapper():
            logs = open(file_log, 'a+', encoding='utf-8')
            func_info = func.__name__, 'вызвана', dt.strftime('%d.%m %H:%M:%S'), '\n'
            func_info = ' '.join(func_info)
            logs.write(func_info)
            logs.close()
            return func
        return wrapper()
    return write_logs

@func_log(file_log='log.txt')
def func():
    print('запуск функции')
