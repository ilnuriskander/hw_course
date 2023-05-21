# формируем словарь из всех римских чисел и новых комбинаций
all_roman = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]

# функция перевода чисел в римскую систему счисления
def to_roman(num):
    # на старте в римском числе ничего нет
    roman = ''
    # пока наше число больше нуля
    while num > 0:
        # перебираем все пары из словаря
        for i, r in all_roman:
            # пока наше число больше или равно числу из словаря
            while num >= i:
                # добавляем соответствующую букву в римское число
                roman += r
                # вычитаем словарное число из нашего числа
                num -= i
    # как все циклы закончились — возвращаем римское число
    return roman

