#ДЗ на понедельник (Chebeyko_Sergey_Lesson_10.py)
# 1. На входе пользователь вводит несколько чисел через пробел.
# На выходе - количество чисел, которые не повторяются.
# 2. На входе пользователь дважды вводит несколько чисел через пробел.
# На выходе - количество чисел, которые содержатся одновременно в первом и втором множестве.
# 3. На входе пользователь дважды вводит несколько чисел через пробел.
# На выходе - вывести совпадающие числа в порядке возрастания
# 10 20 1 2 3 4 7 5 --> 1 2 3 4 5 7 10 20
# 4. (Дополнительно) На входе пользователь вводит несколько чисел через пробел. На выходе
# - вывести все числа в столбик, напротив каждого написать слово
# "Встречалось" или "Не встречалось", если число уже было в последовательности.
# 1 2 3 4 4 3 2 1
# 1 не встречалось
# 2 не встречалось
# 3 не встречалось
# 4 не встречалось
# 4 встречалась
# 3 встречалась
# 2 встречалась
# 1 встречалась
# 5. (дополнительно) Есть текст. Пользователь ничего не вводит.
# На выходе указать, сколько различных слов было в тексте (знаки пунктуации не учитывать,
# программа не должна быть чувствительна к регистру).

print("\033[1m\033[43m\033[42m""Домашнее задание №10, Чебейко Сергей Леонидович""\033[0m")

print('1. На входе пользователь вводит несколько чисел через пробел.\n'
       'На выходе - количество чисел, которые не повторяются.')

a = set(input('Введите числа, разделяя пробелом: ').split())
print(len(a))

print('2. На входе пользователь дважды вводит несколько чисел через пробел.\n'
      'На выходе - количество чисел, которые содержатся одновременно в первом и втором множестве.')

a = set(input('Введите числа, 1-го множества, разделяя пробелом: ').split())
b = set(input('Введите числа, 2-го множества, разделяя пробелом: ').split())
print(len(a.intersection(b)))

print('3. На входе пользователь дважды вводит несколько чисел через пробел.\n'
      'На выходе - вывести совпадающие числа в порядке возрастания\n'
      '10 20 1 2 3 4 7 5 --> 1 2 3 4 5 7 10 20')

a = set(input('Введите числа, 1-го множества, разделяя пробелом: ').split())
b = set(input('Введите числа, 2-го множества, разделяя пробелом: ').split())
c = list(a.intersection(b))
c.sort()
c.sort(key = len)
print(*c, end = ' ')

print('4. (Дополнительно) На входе пользователь вводит несколько чисел через пробел.\n'
      'На выходе - вывести все числа в столбик, напротив каждого написать слово\n'
      '"Встречалось" или "Не встречалось", если число уже было в последовательности.\n'
      '1 2 3 4 4 3 2 1\n'
      '1 не встречалось\n'
      '2 не встречалось\n'
      '3 не встречалось\n'
      '4 не встречалось\n'
      '4 встречалась\n'
      '3 встречалась\n'
      '2 встречаласьn\n'
      '1 встречалась')

a = input('Введите числа, разделяя пробелом: ').split()
b = set()
for i in a:
      if i in b:
            print(f' {i} Встречалось')
      else:
            print(f' {i} Не встречалось')
            b.add(i)

print('5. (дополнительно) Есть текст. Пользователь ничего не вводит.\n'
      'На выходе указать, сколько различных слов было в тексте (знаки пунктуации не учитывать,\n'
      'программа не должна быть чувствительна к регистру).')

import string
a = 'Солнце клонится к обеду обеду, я с горы на попе еду еду, заезжаю я у хату хату и там тадам!㋛'
b = string.punctuation
for i in b:
    if i in a:
        a = a.lower()
        a = a.replace(i, '')
a = set(a.split())
print(len(a))