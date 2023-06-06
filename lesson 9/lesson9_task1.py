# Дан текстовый файл test_file/task1_data.txt
# Он содержит текст, в словах которого есть цифры.
# Необходимо удалить все цифры и записать получившийся текст в файл test_file/task1_answer.txt


file = open('test_file/task1_data.txt', 'r', encoding='utf-8')
file = file.read()
file_list = list(file)
for i in file_list[::-1]:
    if i in '0123456789':
        file_list.remove(i)
a = ''.join(file_list)
new_file = open('test_file/task1_answer.txt', 'w', encoding='utf-8')
new_file.write(a)
new_file.close()


with open("test_file/task1_answer.txt", 'r', encoding='utf-8') as file1:
    with open("test_file/task1_ethalon.txt", 'r', encoding='utf-8') as file2:
        answer = file1.readlines()
        ethalon = file2.readlines()
        assert answer == ethalon, "Файл ответа не совпадает с эталонном"
print('Всё ок')