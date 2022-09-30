# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# num = int(input('Введите номер дня недели: '))
# if (num < 1 or num > 7):
#     print('Введены некорректные данные')
# elif (num==6 or num==7):
#     print('Да')
# else:
#     print('Нет')


# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# x = float(input('Введите координату x: '))
# y = float(input('Введите координату y: '))
# if x == 0 or y == 0:
#     print('Точка лежит на координатной оси')
# elif (x > 0 and y > 0):
#     print('1 четверть')
# elif (x < 0 and y > 0):
#     print('2 четверть')
# elif (x < 0 and y < 0 ):
#     print('3 четверть')
# elif (x > 0 and y < 0):
#     print('4 четверть')


# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
# n = int (input('Введите номер четверти: '))
# if n < 1 or n > 4:
#     print('Введены некорректные данные')
# elif n == 1:
#     print('x > 0, y > 0')
# elif n == 2:
#     print('x < 0, y > 0')
# elif n == 3:
#     print('x > 0, y < 0')
# elif n == 4:
#     print('x > 0, y < 0')


# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# import math


# x1 = float(input('Введите координату x1: '))
# y1 = float(input('Введите координату y1: '))
# x2 = float(input('Введите координату x2: '))
# y2 = float(input('Введите координату y2: '))
# d = float(math.sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2)))
# d = round(d, 2)
# print(d)


# Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат
# def logical_statement (x, y, z):
#     print(f"¬({x} ⋁  {y} ⋁  {z}) = {x} ⋀ ¬ {y} ⋀ ¬ {z} is  {(not (x or y or z)) == (not x and not y and not z)}")
#     return (not (x or y or z)) == (not x and not y and not z)
# if (logical_statement(0, 0, 0) and logical_statement(0, 0, 1) and logical_statement(0, 1, 0) and 
# logical_statement(0, 1, 1) and logical_statement(1, 0, 0) and logical_statement(1, 0, 1) and
# logical_statement(1, 1, 0) and logical_statement(1, 1, 1)):
#     print("Истинно")
# else:
#     print("Ложно")