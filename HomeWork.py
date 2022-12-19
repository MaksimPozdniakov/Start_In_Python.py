# 1. В этой игре человек загадывает число, а компьютер пытается его угадать.
# В начале игры человек загадывает число от 1 до 100 в уме или записывает его на листок бумаги. Компьютер начинает его
# отгадывать предлагая игроку варианты чисел. Если компьютер угадал число, игрок выбирает “победа”. Если компьютер назвал
# число меньше загаданного, игрок должен выбрать “загаданное число больше”. Если компьютер назвал число больше, игрок
# должен выбрать “загаданное число меньше”. Игра продолжается до тех пор пока компьютер не отгадает число.

# import random
#
# user_number = int(input('Загадайте число: '))
# min_number = 1
# max_number = 100
# sing = None
#
# while sing != '=':
#     computer_number = random.randint(min_number, max_number)
#     print(computer_number)
#     sing = input('Укажите >, <, =: ')
#
#     if sing == '>':                           # загаданное число больше предложенного компьютером
#         min_number = computer_number + 1
#     elif sing == '<':                           # загаданное число меньше предложенного компьютером
#         max_number = computer_number - 1
# print('Компьютер угадал число!')

# Еще раз перерешиваем задчи!

# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

# my_number = float(input('Введите число: '))
# my_number = 0.56
# str_my_number = str(my_number)
# list_my_number = list(str_my_number)
# sum = 0
#
# for i in list_my_number:
#     if i == '.':
#         list_my_number.remove('.')
#
# for i in list_my_number:
#     sum += int(i)
#
# print(sum)

# Задайте список из n чисел последовательности (1 + 1/n)^n, выведите его на экран, а так же сумму элементов списка.
# Пример:
# Для n=4 -> [2, 2.25, 2.37, 2.44]
# Сумма 9.06

# num = 4
# new_number = 0
# my_list = []
# for n in range(1, num+1):
#     new_number = (1 + 1/n)**n
#
#     if new_number - int(new_number) == 0:
#         new_number = int(new_number)
#
#     my_list.append(round(new_number, 2))
#
# print(my_list)

# Реализуйте алгоритм перемешивания списка. НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, максимум использование
# библиотеки Random для и получения случайного int

import random
# size_list = int(input('Введите размер нашего списка: '))
# my_list = [random.randint(-10, 10) for i in range(size_list)]
my_list = [-10, -9, 4, -8, 3, -10, 9, 10, -10, -7]
copy_list = my_list[:]

for i in range(len(copy_list)):
    random_index = random.randint(0, len(copy_list) - 1)
    copy_list[i], copy_list[random_index] = copy_list[random_index], copy_list[i]

print(f'Наш изначальный список: {my_list}')
print(f'Наш перемешанный список: {copy_list}')


















