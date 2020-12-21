# Третьяков Роман Викторович
# Факультет Geek University Python-разработки. Основы языка Python
# Урок 5. Задание 4:
# Создать (не программно) текстовый файл со следующим содержимым:
#
# One — 1
# Two — 2
# Three — 3
# Four — 4
#
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен
# записываться в новый текстовый файл.


dict_num = {'One': 'Один',
            'Two': 'Два',
            'Three': 'Три',
            'Four': 'Четыре',
            'Five': 'Пять'}

with open('task-04-eng.txt', 'r') as eng_file:
    with open('task-04-rus.txt', 'w') as rus_file:
        for i in eng_file:
            eng_num = i.strip().split(' - ')

            rus_file.write(dict_num.get(eng_num[0]) + ' - ' + eng_num[1] + '\n')