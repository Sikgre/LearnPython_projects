print('Задание 1')
numbers_list = [9, 19, 29, 39, 49, 59, 69, 79, 89, 99]

for number in numbers_list:
    print(number + 1)

print('--------')
print('Задание 2')
text = input('Введите текст: ')

for vertical_text in text:
    print(vertical_text)

print('---------')
print('Задание 3')

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

#for sch_class in school_scores['school_class']
#sum(school_scores[1]['scores']) = len(chool_scores[1]['scores'])


# import statistics
# from discounted import discounted

# for number in range(3):
#     print(f'Привет, мир {number}!')

# for letter in 'python':
#     print(letter.upper())

# example_string = 'Я учу язык python'

# for word in example_string.split():
#     print(f'Длина слова "{word}": {len(word)}')

# students_scores = [1, 21, 19, 6, 5]

# print(f'Средняя оценка: {statistics.mean(students_scores)}')

# for score in students_scores:
#     print(score)

# scores_sum = 0
# for score in students_scores:
#     scores_sum = scores_sum + score
#     print(scores_sum)

# print(f'Средняя оценка: {scores_sum/len(students_scores)}')

# stock = [
# 		{'name': 'iPhone Xs Plus', 'stock': 24, 'price': 65432.1,
#                 'discount': 25},
# 		{'name': 'Samsung Galaxy S10', 'stock': 8, 'price': 50000.0,
#                 'discount': 10},
# 		{'name': '', 'stock': 18, 'price': 10000.0, 'discount': 10}
# ]

# for phone in stock:
#     print(phone)
#     phone["final_price"] = discounted(phone["price"], phone["discount"], name = phone["name"])
#     print(phone)
#     print("---")

# print(stock)


