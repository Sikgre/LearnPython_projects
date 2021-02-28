"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""

#при чтении целиком
# def main():
#     """
#     Эта функция вызывается автоматически при запуске скрипта в консоли
#     В ней надо заменить pass на ваш код
#     """
#     with open("referat.txt", 'r', encoding='UTF-8') as file:
#         referat = file.read()

#     print(f'Длина строки: {len(referat)}')
#     print(f'Число слов: {len(referat.split())}')

#     ref_with_shouts = referat.replace('.', '!')
#     print(ref_with_shouts)
#     with open('referat2.txt', 'w', encoding = 'UTF-8') as file2:
#         file2.write(ref_with_shouts)


#при чтении построчно

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    line_lenght = 0
    words = 0
    
    with open("referat.txt", 'r', encoding='UTF-8') as file:
        for line in file:
            referat = file.read()
            line_lenght += len(referat)
            words += len(referat.split())

    print(f'\nДлина строки: {line_lenght}')
    print(f'Число слов: {words}\n')

    ref_with_shouts = referat.replace('.', '!')
    print(ref_with_shouts)

    with open('referat2.txt', 'w', encoding = 'UTF-8') as file2:
        file2.write(ref_with_shouts)

if __name__ == "__main__":
    main()
