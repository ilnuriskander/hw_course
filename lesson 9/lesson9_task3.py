# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

# Здесь пишем код
file = open('test_file/task_3.txt', 'r', encoding='utf-8')
file = file.read()
file_list = file.split('\n\n')
new_list = []
for i in range(len(file_list)):
    file_list2 = file_list[i].split('\n')
    file_list2 = [int(j) for j in file_list2]
    pokupka = sum(file_list2)
    new_list.append(pokupka)
sort_popupki = sorted(new_list, reverse=True)
three_most_expensive_purchases = sum(sort_popupki[:3])

assert three_most_expensive_purchases == 202346