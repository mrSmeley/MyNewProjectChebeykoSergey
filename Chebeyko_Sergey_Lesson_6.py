#ДЗ на четверг:
# Казино. Компьютер генерирует числа от 1 до 10 и от 1 до 2-х соответственно.
# Цифры от одного до 10 отвечают за номера, а от 1 до 2 за цвета(1-красный,2 черный).
# Пользователю дается 5 попыток угадать номер и цвет(Прим. введения с клавиатуры: 3 красный).
# В случае неудачи (не угадали за 5 попыток) вывести на экран правильную комбинацию.
# random.choice(['red','black']) #choice выбирает случайную строку из этого списка
# Имя файла Chebeyko_Sergey_Lesson_6.py. Сдать работу до четверга!

print("\033[1m\033[43m\033[42m""Домашнее задание №5, Чебейко Сергей Леонидович""\033[0m")

from random import random

n = round(random() * 10)
print('Число заданное компьютером', [n]) # "n" заданное число компьютером,
# можно и убрать загаданное число компьютером.
i = 1
print("Компьютер загадал число. Отгадайте его. У вас есть 5 попыток")
while i <= 5:
    a = int(input(str(i) + '-я попытка: '))
    if a > n:
        print('Много')
    elif a < n:
        print('Мало')
    else:
        print('Поздравляю вы угадали с %d-й попытки, \033[4m\033[46m\033[30mUser_Name:)!\033[0m.' % i)
        break
    i += 1
else:
    print('\033[31m''ERROR>>>>>>>>>>>\033[0m. \033[35m<(o.O,)>\033[0m.'"Вы использовали 5 попыток, попробуйте ещё раз")
import random
h = ['\033[31m '"red" '\033[0m', "black"]
print("Правильный ответ: ", n,  random.choice(h))