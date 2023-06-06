import datetime
dt = datetime.datetime.now()

def func_log(func, file_log='log.txt'):
    def wrapper():
        logs = open(file_log, 'a+', encoding='utf-8')
        logs.write(func())
        logs.close()
        return wrapper()

@func_log
def f():
    a = f.__name__, 'вызвана', dt.strftime('%d.%m %H:%M:%S')
    b = ' '.join(a)
    return b

f()
