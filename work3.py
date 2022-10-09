# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# mylist = [2, 3, 5, 9, 3]
# sum = 0
# for i in range(len(mylist)):
#     if i % 2 == 1:
#         sum = sum + mylist[i]
# print(sum)



# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# mylist = [2, 3, 4, 5, 6]
# newlist = []
# n = len(mylist) - 1
# count = 0
# for i in range(len(mylist)):
#     while (i+count)<=(n-count):
#         newlist.append (mylist[i+count] * mylist[n-count])
#         count=count+1
# print(newlist)



# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# num = int(input('Введите десятичное число: '))
# count = 0
# binnum = 0
# while num >= 1:
#     if count == 0:
#         count = 1
#     else:
#         binnum = binnum + (num % 2) * count
#         count = count * 10
#         num = int (num / 2)
# print(int(binnum))



# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# n = int(input('Введите количество элементов: '))
# list = [0, 1]
# for i in range(2, n + 1):
#     list.append(list[i-2]+list[i-1])
# for i in range(0, -n+1, -1):
#     list.insert(0, list[1]-list[0])
# print(list)




# import decimal
# from hashlib import new
# import random
# import math
# num = int(input('Введите размер списка: '))
# mylist = []
# k = random.randint(1, 4)
# for i in range(num):
#     mylist.append(float(decimal.Decimal(f'{round(random.uniform(-10, 10), k)}')))
# newlist = []
# for i in range(len(mylist)):
#     if abs(mylist[i]) - abs(int(mylist[i])) != 0.0:
#         newlist.append(round((abs(mylist[i]) - abs(int(mylist[i]))), 4))
# print(newlist)
# max_ell = newlist[0]
# min_ell = newlist[0]
# for i in range(len(newlist)):
#     if newlist[i] > max_ell:
#         max_ell = newlist[i]
#     if newlist[i] < min_ell:
#         min_ell = newlist[i]
# print(max_ell, min_ell)
# print(max_ell - min_ell)
