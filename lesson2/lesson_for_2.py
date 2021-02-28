names = ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]
l = 0
name = 0

def search_name(name):
    name = input("Введите имя: ")
    for l in range(len(names)):
        if names[l] == name:
            print(f' Имя {name} есть в списке')

search_name(name)
