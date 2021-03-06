# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Петя'},
]
  
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

student = [student['first_name'] for student in students]
names = set(student)
for name in names:
  print(f'{name}: {student.count(name)}')


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Оля'},
]

# Пример вывода:
# Самое частое имя среди учеников: Маша

student = [student['first_name'] for student in students]

def most_common(my_list):
    return max(set(my_list), key = my_list.count)

print(f'\nСамое частое имя среди учеников: {most_common(student)}\n')

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
school_students = [
  [  # это – первый класс
    {'first_name': 'Вася'},
    {'first_name': 'Вася'},
  ],
  [  # это – второй класс
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
  ]
]

# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

class_1 = [student['first_name'] for student in school_students[0]]
class_2 = [student['first_name'] for student in school_students[1]]
print(f'Самое частое имя в 1-м классе: {most_common(class_1)}')
print(f'Самое частое имя во 2-м классе: {most_common(class_2)}\n')


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}

# Пример вывода:
# В классе 2a 2 девочки и 0 мальчика.
# В классе 3c 0 девочки и 2 мальчика.

for klass, item in enumerate(school):
  count_boys = 0
  count_girls = 0
  students = school[klass]['students']
  student = [student['first_name'] for student in students]
  for name in student:
    if is_male.get(name) is True:
      count_boys += 1
    else:
      count_girls += 1
  print(f'В классе {school[klass]["class"]} {count_boys} мальчиков и {count_girls} девочек')
  

# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}

# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

boys_class = list()
girls_class = list()
for klass, item in enumerate(school):
  count_girls = 0
  count_boys = 0
  students = school[klass]['students']
  student = [student['first_name'] for student in students]
  for name in student:
    if is_male.get(name) is True:
      count_boys += 1
    else:
      count_girls += 1
  boys_class.append(count_boys)
  girls_class.append(count_girls)

print(f'\nБольше всего мальчиков в классе ' + school[boys_class.index(max(boys_class))]['class'])
print(f'Больше всего девочек в классе ' + school[girls_class.index(max(girls_class))]['class'])
