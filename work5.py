# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# text = input('Введите текст через пробел: ')
# print('Исходный текст: ', text)
# text = text.split()
# find = 'абв'
# new_text = []

# for i in text:
#     if find not in i:
#         new_text.append(i)

# text_2 = ' '.join(new_text) 
# print('Полученный текст: ', text_2)



# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. Входные и выходные данные хранятся в отдельных текстовых файлах.

# with open('file_encode.txt', 'w') as data:
#     data.write('aaaaaaabbbbbbcccccccccd')

# with open('file_encode.txt', 'r') as data:
#     string = data.readline()

# def rle_encode(decoded_string):
#     encoded_string = ''
#     count = 1
#     char = decoded_string[0]
#     for i in range(1, len(decoded_string)):
#         if decoded_string[i] == char:
#             count += 1
            
#         else:
#             encoded_string = encoded_string + str(count) + char
#             char = decoded_string[i]
#             count = 1
#     encoded_string = encoded_string + str(count) + char
#     return encoded_string


# def rle_decode(encoded_string):
#     decoded_string = ''
#     char_amount = ''
#     for i in range(len(encoded_string)):
#         if encoded_string[i].isdigit():
#             char_amount += encoded_string[i]
#         else:
#             decoded_string += encoded_string[i] * int(char_amount)
#         char_amount = ''
#     print(decoded_string)

#     return decoded_string


# with open('file_encode.txt', 'r') as file:
#     decoded_string = file.read()

# with open('file_decode.txt', 'w') as file:
#     encoded_string = rle_encode(decoded_string)
#     file.write(encoded_string)

# print('Decoded string: \t' + decoded_string)
# print('Encoded string: \t' + rle_encode(decoded_string))


# Создайте программу для игры в 'Крестики-нолики'.


# from tkinter import *

# frm = []; btn = []; who = True
# playArea = []
# standings = []  
# def play(n):
#     global who
#     btn[n].config(text= 'X' if who else 'O', state=DISABLED)
#     playArea[n] = 1 if who else -1
#     standings[0] = playArea[0] + playArea[1] + playArea[2]
#     standings[1] = playArea[3] + playArea[4] + playArea[5]
#     standings[2] = playArea[6] + playArea[7] + playArea[8]
#     standings[3] = playArea[0] + playArea[3] + playArea[6]
#     standings[4] = playArea[1] + playArea[4] + playArea[7]
#     standings[5] = playArea[2] + playArea[5] + playArea[8]
#     standings[6] = playArea[0] + playArea[4] + playArea[8]
#     standings[7] = playArea[2] + playArea[4] + playArea[6]
#     print(n, standings[0:8])
#     for i in range(8):
#         if standings[i] == 3:
#             print('X win')
#         elif standings[i] == -3:
#             print('O win')
#     who = not(who)

# for i in range(3):
#     frm.append(Frame())
#     frm[i].pack(expand=YES, fill=BOTH)
#     for j in range(3):
#         btn.append(Button(frm[i], text=' ', font=('mono', 20, 'bold'), width=3, height=2))
#         btn[i*3+j].config(command=lambda n=i*3+j:play(n))
#         btn[i*3+j].pack(expand=YES, fill=BOTH, side=LEFT, padx=1, pady=1)
#         playArea.append(0)
#         standings.append(0)

# mainloop()


# Создайте программу для игры с конфетами человек против человека.

# import random
# import os

# def player_vs_bot():
#     candies_total = 150
#     max_take = 28
#     player_1 = input('\nКак тебя зовут?: ')
#     player_2 = 'Компьютер'
#     players = [player_1, player_2]
#     print(f'\n Привет, {player_1} и  {player_2}\n')
#     print('\nДля начала опеределим кто первый начнет игру.\n')

#     lucky = random.randint(-1, 0)

#     print(f'Поздравляю {players[lucky+1]} ты ходишь первым !')

#     while candies_total > 0:
#         lucky += 1

#         if players[lucky % 2] == 'Компьютер':
#             print(
#                 f'\nХодит {players[lucky%2]} \nНа кону {candies_total}. \n')

#             if candies_total < 29:
#                 step = candies_total
#             else:
#                 delenie = candies_total//28
#                 step = candies_total - ((delenie*max_take)+1)
#                 if step == -1:
#                     step = max_take -1
#                 if step == 0:
#                     step = max_take
#             while step > 28 or step < 1:
#                 step = random.randint(1,28)
#             print(step)
#         else:
#             step = int(input(f'\nНу чтож ходи,  {players[lucky%2]} \nНа кону {candies_total}\n '))
#             while step > max_take or step > candies_total:
#                 step = int(input(f'\nЗа один ход можно взять {max_take} конфет, попробуй еще раз: '))
#         candies_total = candies_total - step

#     print(f'На кону осталось {candies_total} \nПобедил {players[lucky%2]}')

# player_vs_bot()
