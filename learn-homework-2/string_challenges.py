# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])


# Вывести количество букв "а" в слове
from collections import Counter

word = 'Архангельск'
words_a = Counter(word)['а']
print(words_a)


# Вывести количество гласных букв в слове
word = 'Архангельск'
glasnie = ['а' , 'у' , 'о' , 'ы' , 'и' , 'э' , 'я' , 'ю' , 'ё' , 'е']
number = 0
count_characters = 0
for number in word.lower():
    if number in glasnie:
        count_characters += 1

print(count_characters)


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
sentence_words = sentence.split()
count_words = len(sentence_words)
print(count_words)


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
sentence_words = sentence.split()
for characters in sentence_words:
    print(characters[0])


# Вывести усреднённую длину слова.
sentence = 'Мы приехали в гости'
sentence_words = sentence.split()
sum_length = 0
for words in sentence_words:
    sum_length += len(words)
avg_lenght = sum_length / len(sentence_words)
print(f'Усреднённая длина слова равна {avg_lenght} символов')