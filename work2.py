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
# def mix_list(list_original):
#     list = list_original[:]
#     list_length = len(list)
#     for i in range(list_length):
#         index = random.randint(0, list_length - 1)
#         temp = list[i]
#         list[i] = list[index]
#         list[index] = temp
#     return list
# list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# mixed_list = mix_list(list)
# print("Исходный список: ")
# print(list)
# print("Перемешанный список: ")
# print(mixed_list)

