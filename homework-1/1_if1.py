"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить 
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат 
  работы функции в переменную
* Вывести содержимое переменной на экран

"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    age = float(input('Введите ваш возраст: '))

    def occupation(age):
        if 3 <= age < 7:
            return 'Вы учитесь в детском саду.'
        elif 7 <= age < 18: #так в данном случае писать не обязательно; можно просто age < 18 и т.д. Код будет короче, но не нагляднее. 
            return 'Вы учитесь в школе.'
        elif 18 <= age < 23:
            return 'Вы учитесь в ВУЗе.'
        elif 23 <= age < 65:
            return 'Вы работаете.'
        else:
            return 'Вы указали возраст меньше 3, либо больше или равно 65 лет, либо нечисловое значение.'

    answer = occupation(age)
    print(answer)


if __name__ == "__main__":
    main()
