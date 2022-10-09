# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда (1, 1*2, 1*2*3, 1*2*3*4)

# import math


# num = int(input ('Введите натуральное число: '))
# list=[]
# for i in range(1, num + 1):
#     import math
#     list.append(math.factorial(i))
# print (list)



# Задайте список из n чисел последовательности (1+1/n)^n
# Выведитте на экран саму последовательность и сумму элеементов этой последовательности (для проверки сумма для 4 элементов = 9,06 (примерно))
# i = int(input('Введите натуральное число: '))
# list=[]
# sum = 0
# for n in range(1, i+1):
#     list.append((1+(1/n))**n)
#     sum = round ((sum + (1+(1/n))**n), 2)
# print(list)
# print(sum)



# Реализуйте алгоритм перемешивания списка, без использования встроеных методов (особенно SHUFFLE, без него) можно (нужно) использовать библиотеку Random

# import random
# newlist=[]
# list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# for i in range(len(list)):
#     index = random.randint(0, len(list) - 1)
#     newlist.append(list[index])
# print("Исходный список: ")
# print(list)
# print("Перемешанный список: ")
# print(newlist)


# Напишите программу, которая находит сумму цифр числа.

# num = float(input('Введите число: '))
# num = str(num)
# sum = 0
# for i in num:
#     if i.isdigit():
#         sum += int(i)
# print(sum)


# path = 'file.txt'
# import random
# num = int(input('Введите размер массива: '))
# mylist=[]
# for _ in range(num):
#     mylist.append(random.randint(-num, num))
# print(mylist)
# data=open (path, 'r')
# f1=data.readline()[:-1]
# f2=data.readline()
# data.close
# print(f1, end = " ")
# print(f2, end = " ")
# print(mylist[int(f1)]*mylist[int(f2)])


# path = 'file.txt'
# with open(path, 'w', encoding='UTF-8') as data:
#     data.write('Привет')