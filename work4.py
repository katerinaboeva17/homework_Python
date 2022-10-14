# Вычислить число ПИ c заданной точностью *d*

# import math

# d = float(input('Введите шаблон числа: '))
# count = 0
# while(d != int(d)):
#     d = d * 10
#     count += 1
# print(round(math.pi, count))



# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# num = int(input('Введите натуральное число: '))
# list = []
# k = 2
# while(num >= 2):
#     if(num % k == 0):
#         num = num / k
#         list.append(k)
#     else:
#         k = k + 1
# print(list)


# Задайте последовательность цифр. Напишите программу, которая выведет список неповторяющихся элементов
# исходной последовательности.

# import random
# list = {}
# string = " "
# mylist = "".join(list(map(str, [random.randint(0, 10) for i in range(20)])))
# for c in mylist:
#     if list.get(c):
#         list[c] = list.get(c) + 1
#     else:
#         list[c] = 1
# for k, v in list.items():
#     if v == 1:
#         string += str(k) + " "
# print (f'Неповторяющиеся элементы {string}') if string else print('Неповторяющихся элементов нет')



# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от -100 до 100)
# многочлена и записать в файл многочлен степени k
# k - максимальная степень многочлена, следующий степень на 1 меньше и так до ноля
# Коэффициенты расставляет random, поэтому при коэффициенте 0 просто пропускаем данную итерацию степени

# from msvcrt import kbhit
# from random import randint as rI

# def createDict():
#     equation = {}
#     degree = int(input("Введите максимальную степень: "))
#     for i in range (degree, -1, -1):
#         equation[i] = rI(-20,20)
#     return equation


# def createEquation(equation: dict):
#     equation  = createDict()
#     strEquation = ''
#     first  = True

#     for k, v in equation.items():
#         if first:
#             first  = False
#             if v > 0:
#                 strEquation += f'{v}*x^{k}'
#             elif v < 0:
#                 strEquation += f'-{abs(v)}*x^{k}'
#         else:
#             if  v > 0:
#                 strEquation += f' + {v}*x^{k}'
#             elif v < 0:
#                 strEquation += f' - {abs(v)}*x^{k}'

#     return strEquation

# def printEquation(equation: str):
#     print(equation.replace('*x^1', 'x').replace('*x^0', '') + ' = 0')
    
   
# def parseEquation(equation: str):
#     eqDict = {}
#     equation = equation.replace('+', ' ').replace(' - ', ' -')
#     equation = equation.split()

#     for i in equation:
#         element = i.split('*x^')
#         eqDict[int(element[1])] = int(element[0])
#     return eqDict



# def summEquation(equation1: dict, equation2: dict):
#     finalEquation = {}

#     for i in range(max(len(equation1), len(equation2)), -1, -1):
#         if equation1.get(i) or equation2.get(i):
#             finalEquation[i] = (equation1.get(i) if equation1.get(i) else 0) + (equation2.get(i) if equation2.get(i) else 0)
#     return finalEquation

# equation1 = createDict()
# equation2 = createDict()

# finalEquation = summEquation(equation1, equation2)
# printEquation(createEquation(equation1))
# printEquation(createEquation(equation2))
# printEquation(createEquation(finalEquation))
    

