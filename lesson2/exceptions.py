print('Задание 1')

def hello_user():
    while True:
        try:
            answer = input('Как дела? ')
            if answer == 'Хорошо':
                break
            else:
                answer
        except KeyboardInterrupt:
            print('')
            print('Пока!')
            break      

hello_user()


print('Задание 2')

def discounted(price, discount, max_discount=20):
    try:
        price = abs(float(price))
        discount = abs(float(discount))
        max_discount = abs(int(max_discount))
        if max_discount > 99:
            print('Слишком большая максимальная скидка')
        if discount >= max_discount:
            return price
        else:
            return price - (price * discount / 100)
    except (ValueError, TypeError):
        print('Введено некорректное значение')

print(discounted(100, 19))
print('--------')
print(discounted(100, 21))
print('--------')
print(discounted(100, 30, 15))
print('--------')
print(discounted(0, None))
print('--------')
print(discounted(100, 'a'))
print('--------')
print(discounted(100, 20, 'a'))
print('--------')
print(discounted(True, False, False))