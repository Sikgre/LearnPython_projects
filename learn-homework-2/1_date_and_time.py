"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""

from datetime import datetime, date, time, timedelta

def print_days():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    today = date.today()
    d_1 = timedelta(days=1)
    yesterday = today - d_1
    days_30_ago = today - 30*d_1
    print(today)
    print(yesterday)
    print(days_30_ago) 


def str_2_datetime(date_string):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    print(datetime.strptime(date_string, "%d/%m/%y %H:%M:%S.%f"))

if __name__ == "__main__":
    print_days()
    str_2_datetime("01/01/20 12:10:03.234567")
