print('Задание 1')

def hello_user():
    try:
    while True:
        answer = input('Как дела? ')
        if answer == 'Хорошо':
            break
        else:
            answer

hello_user()

print('')
print('Задание 2')

ask_answer = [
    {"ask": 'Привет', "answer": 'Привет'},
    {"ask": 'Как дела?', "answer": 'Хорошо'},
    {"ask": 'Что делаешь?', "answer": 'Работаю'},
    {"ask": 'Как работа?', "answer": 'Прекрасно!'},
    {"ask": 'Как семья, дети?', "answer": 'Отлично!'}
]

d = 0
ask = 0

def ask_user(ask):
    while True:
        print('')
        ask = input('Введите ваш вопрос: ')
        for d in range(len(ask_answer)):
            if ask == ask_answer[d]["ask"]:
                print('')
                print(f'Пользователь: {ask_answer[d]["ask"]}')
                print(f'Программа: {ask_answer[d]["answer"]}')
                print('')
            else:
                ask

ask_user(ask)
