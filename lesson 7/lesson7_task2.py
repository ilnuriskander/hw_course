# Напишите класс PersonInfo
# Экземпляр класса создается из следующих атрибутов:
# 1. Строка - "Имя Фамилия"
# 2. Число - возраст сотрудника
# 3. Подразделения от головного до того, где работает сотрудник.
# Реализуйте методы класса:
# 1. short_name, который возвращает строку Фамилия И.
# 2. path_deps, возвращает путь "Головное подразделение --> ... --> Конечное подразделение"
# 3. new_salary, Директор решил проиндексировать зарплаты, и новая зарпалата теперь вычисляет по формуле:
# 1337*Возраст*суммарное кол-во вхождений трех наиболее часто встречающихся букв из списка подразделений
# (регистр имеет значение "А" и "а" - разные буквы)
# Например (Ввод --> Вывод) :
# PersonInfo('Александр Шленский',
#            32,
#            'Разработка', 'УК', 'Автотесты').short_name() --> 'Шленский А.'
# PersonInfo('Александр Шленский',
#            32,
#            'Разработка', 'УК', 'Автотесты').path_deps() -->
#            'Разработка --> УК --> Автотесты'
# PersonInfo('Александр Шленский', 32, 'Разработка', 'УК', 'Автотесты').new_salary() --> 385056 т.к.
# т.к. буква "т" встречается 4 раза, "а" 3 раза, 'о' 2 раза, остальные по одной. Сумма трёх самых частых букв 4+3+2 = 9.
# 1337*32*9 = 385056

# Здесь пишем код
class PersonInfo:
    def __init__(self, fio, age, *department):
        self.fio = fio
        self.age = age
        self.department = department

    def short_name(self):
        list_fio = self.fio.split()
        list_name = list(list_fio[0])
        name_str = list_fio[1] + ' ' + list_name[0] + '.'
        return name_str


    def path_deps(self):
        b = []
        for i in self.department:
            b.append(i)
        b = ' --> '.join(b)
        return b

    def new_salary(self):
        a = list(''.join(self.department))
        letters_dict = {}
        for letter in a:
            letters_dict[letter] = letters_dict.get(letter, 0) + 1
        points_all = sorted(letters_dict.values(), reverse=True)
        points_max = sum(points_all[:3])
        solary = 1337 * self.age * points_max
        return solary




# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


first_person = PersonInfo('Александр Шленский', 32, 'Разработка', 'УК', 'Автотесты')
fourth_person = PersonInfo('Иван Иванов', 26, 'Разработка')
second_person = PersonInfo('Пётр Валерьев', 47, 'Разработка', 'УК')
third_person = PersonInfo('Макар Артуров', 51, 'Разработка', 'УК', 'Нефункциональное тестирование', 'Автотестирование')

data = [first_person.short_name,
        second_person.short_name,
        third_person.short_name,
        fourth_person.short_name,

        first_person.path_deps,
        second_person.path_deps,
        third_person.path_deps,
        fourth_person.path_deps,

        first_person.new_salary,
        second_person.new_salary,
        third_person.new_salary,
        fourth_person.new_salary
        ]


test_data = ['Шленский А.', 'Валерьев П.', 'Артуров М.', 'Иванов И.',

             'Разработка --> УК --> Автотесты',
             'Разработка --> УК',
             'Разработка --> УК --> Нефункциональное тестирование --> Автотестирование',
             'Разработка',
             385056, 314195, 1227366, 173810]

for i, d in enumerate(data):
    assert_error = f'Не прошла проверка для метода {d.__qualname__} экземпляра с атрибутами {d.__self__.__dict__}'
    assert d() == test_data[i], assert_error
    print(f'Набор для метода {d.__qualname__} экземпляра класса с атрибутами {d.__self__.__dict__} прошёл проверку')
print('Всё ок')
