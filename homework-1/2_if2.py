"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    def str_function(str1, str2):
      if isinstance(str1, str) and isinstance(str2, str):
          if str1 == str2:
              return '1'
          if len(str1) > len(str2):
              return '2'
          if  str1 != str2 and str2 == 'learn':
              return '3'
          else:
              return '4'
      else:
          return '0'

    print(str_function('learn', 'python')) #4
    print(str_function('python', 'learn')) #2
    print(str_function('pytho', 'learn')) #3
    print(str_function('learn', 'learn')) #1
    print(str_function(0, 1)) #0
    print(str_function(25-4-1999, 25-5-1999)) #0

   
if __name__ == "__main__":
    main()
