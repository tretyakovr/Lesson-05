# Третьяков Роман Викторович
# Факультет Geek University Python-разработки. Основы языка Python
# Урок 5. Задание 7:
# Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о
# фирме: название, форма собственности, выручка, издержки.
#
# Пример строки файла: firm_1 ООО 10000 5000.
#
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
#
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь
# со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
#
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
#
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
#
# Пример json-объекта:
#
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджеры контекста.


import json

with open('task-07.txt', 'r') as firm_data:
    firm_lst = [{}, {}]
    total_profit = 0
    profit_count = 0
    for i in firm_data:
        firm_detail = i.strip().split(' ')
        profit = int(firm_detail[2]) - int(firm_detail[3])
        firm_lst[0][firm_detail[0] + ', ' + firm_detail[1]] = profit

        if profit > 0:
            total_profit += profit
            profit_count += 1

    firm_lst[1]['average_profit'] = total_profit / profit_count

print(firm_lst)

with open('task-07.json', 'w', encoding = 'UTF-8') as json_output:
    json.dump(firm_lst, json_output, indent = 4)