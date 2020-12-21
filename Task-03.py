# Третьяков Роман Викторович
# Факультет Geek University Python-разработки. Основы языка Python
# Урок 5. Задание 3:
# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину
# их окладов. Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих
# сотрудников. Выполнить подсчет средней величины дохода сотрудников


min_salary = 20000
total_salary = 0
person_count = 0
person_min_salary = 0

with open('task-03.txt', 'r') as file_txt:

    print(f'Перечень сотрудников с окладом меньше {min_salary}:')
    for line_str in file_txt:
        person = line_str.strip().split(', ')
        person_count += 1
        total_salary += int(person[1])

        if int(person[1]) < min_salary:
            person_min_salary += 1
            print(f'ФИО: {person[0]}, оклад {person[1]}')

    print()
    print(f'Всего сотрудников: {person_count}')
    print(f'Сотрудников с окладом менее {min_salary}: {person_min_salary}')
    print(f'Средняя зп сотрудников: {total_salary/person_count}')