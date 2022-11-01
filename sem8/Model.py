from base64 import encode
from os import remove
import Control



phone_book = []

path = 'sem8\\'

def get_phone_book():
    global phone_book
    return phone_book

def  set_path(file):
    global path
    path += file

def open_file():
    global path
    global phone_book
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
        for item in data:
            contact = item.replace('\n', ''). split(';')
            phone_book.append(contact)

def new_contact(contact):
    global phone_book
    phone_book.append(list(contact))

def change_contact(id, choise, value):
    global phone_book
    phone_book[int(id)][int(choise)] = value

def delete_contact(id: int):
    global phone_book
    phone_book.pop(id)

def write_file():
    global phone_book
    with open('sem8\\new_phone_book.txt', 'w', encoding='UTF-8') as file:
        for id, item in enumerate(phone_book):
            print (id, *item, file=file)

def find_contact(char):
    global phone_book
    flag = True
    for item in phone_book:
        for j in item:
            if (char == j):
                print(*item)
                flag = False
    if flag:
        print('Ничего не найдено.')

