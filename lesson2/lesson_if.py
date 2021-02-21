age = float(input('Введите ваш возраст: '))

def occupation(age):
    if 3 <= age < 7:
        return 'Вы учитесь в детском саду.'
    elif 7 <= age < 18:
        return 'Вы учитесь в школе.'
    elif 18 <= age < 23:
        return 'Вы учитесь в ВУЗе.'
    elif 23 <= age < 65:
        return 'Вы работаете.'
    else:
        return 'Вы указали возраст меньше 3, либо больше или равно 65 лет, либо нечисловое значение.'

answer = occupation(age)
print(answer)


# balance = 11
# price = 10
# print(bool(balance<0 or price > balance))

# if balance<0 or price > balance:
#     print("Пополните свой баланс!")

# if balance > price:
#     print('Спасибо за покупку!')
# else:
#     print('Пожалуйста, пополните баланс!')

# temperature = 30
# if temperature <= 0:
#     print('На улице холодно')
# elif 0 <= temperature < 15:
#     print('На улице прохладно')
# # elif 15 <= temperature < 25:
# #     print('На улице тепло')
# # else:
# #     print('На улице жарко')

# def weather(temperature):
#     if temperature <= 0:
#         return 'На улице холодно'
#     elif 0 <= temperature < 15:
#         return 'На улице прохладно'
#     elif 15 <= temperature < 25:
#         return 'На улице тепло'
#     else:
#         return 'На улице жарко'

# print(weather(-2))
# print(weather(0))
# print(weather(12))
# print(weather(30))

# phone1 = {'name': 'iPhone Xs Plus', 'stock': 24, 'price': 65432.1,
#             'discount': 25}
# phone2 = {'name': 'Samsung Galaxy S10', 'stock': 8, 'price': 50000.0,
#             'discount': 10}
# phone3 = {'name': '', 'stock': 8, 'price': 30000.0,
#             'discount': 10}

# def discounted(price, discount, max_discount=20, name = ""):
#     price = abs(float(price))
#     discount = abs(float(discount))
#     max_discount = abs(float(max_discount))
#     if max_discount > 99:
#         raise ValueError('Слишком большая максимальная скидка')
#     if discount >= max_discount or "iphone" in name.lower() or not name:
#         return price
#     else:
#         return price - (price * discount / 100)

# apple_desc = discounted(phone1["price"], phone1["discount"], name = phone1["name"])
# print(apple_desc)
# android_desc = discounted(phone2["price"], phone2["discount"], name = phone2["name"])
# print(android_desc)
# empty_desc = discounted(phone3["price"], phone3["discount"], name = phone3["name"])
# print(empty_desc)