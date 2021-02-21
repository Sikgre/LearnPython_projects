"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например:
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user() которая с помощью функции input()
  просит пользователя ввести вопрос, а затем, если вопрос есть
  в словаре, программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую
    
"""

questions_and_answers = [
        {"ask": 'Привет', "answer": 'Привет'},
        {"ask": 'Как дела?', "answer": 'Хорошо'},
        {"ask": 'Что делаешь?', "answer": 'Работаю'},
        {"ask": 'Как работа?', "answer": 'Прекрасно!'},
        {"ask": 'Как семья, дети?', "answer": 'Отлично!'}
    ]


def ask_user(questions_and_answers):
    """
    Замените pass на ваш код
    """
    d = 0
    ask = 0
    
    
    while True:
        print('')
        ask = input('Введите ваш вопрос: ')
        for d in range(len(questions_and_answers)):
            if ask == questions_and_answers[d]["ask"]:
                print('')
                print(f'Пользователь: {questions_and_answers[d]["ask"]}')
                print(f'Программа: {questions_and_answers[d]["answer"]}')
                print('')
            else:
                ask


if __name__ == "__main__":
    ask_user(questions_and_answers)
