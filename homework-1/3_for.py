"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    school_scores = [
    {'school_class': '4a', 'scores': [3, 4, 4, 5, 2]},
    {'school_class': '4b', 'scores': [3, 4, 4, 5, 2, 3, 4, 2]},
    {'school_class': '1', 'scores': [2, 3, 4, 5, 2, 3, 4, 5]},
    {'school_class': '2', 'scores': [3, 5, 2, 4, 3]},
    {'school_class': '3', 'scores': [5, 5, 5, 4, 4]}
    ]

    s = school_scores
    c = 0
    sum_class = 0
    count_pupils = 0
    for c in range(len(s)):
        sum_class += sum(s[c]['scores'])
        count_pupils += len(s[c]['scores'])
        print(f"Класс: {s[c]['school_class']}, средний балл: {sum(s[c]['scores'])/len(s[c]['scores'])}")
    print(f"Средний балл по школе: {round(sum_class/count_pupils, 3)}")


if __name__ == "__main__":
    main()
