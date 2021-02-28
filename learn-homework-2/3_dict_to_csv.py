"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""
import csv

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    dict = [
        {'name': 'Маша', 'age': 25, 'job': 'Scientist'}, 
        {'name': 'Вася', 'age': 28, 'job': 'Programmer'}, 
        {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
        {'name': 'Иван', 'age': 30, 'job': 'Worker'},
        {'name': 'Аня', 'age': 50, 'job': 'Secretary'}
    ]
    with open('dict.csv', 'w', encoding='UTF-8') as myfile:
        fields = ['name', 'age', 'job']
        writer = csv.DictWriter(myfile, fields, delimiter = ';')
        writer.writeheader()
        for user in dict:
            writer.writerow(user)


if __name__ == "__main__":
    main()
