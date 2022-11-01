from unicodedata import name


def show_menu():
    print('1. Показать все контакты')
    print('2. Открыть файл с контактами')
    print('3. Записать файл с контактами')
    print('4. Добавить контакт')
    print('5. Изменить контакт')
    print('6. Удалить контакт')
    print('7. Поиск по контактам')
    
    choise = int(input('Выберите пункт меню: '))
    return choise

def show_phone_book(phone_book):
        if len(phone_book) < 1:
            print('Телефонная книга пуста')
        else:
            for id, item in enumerate(phone_book):
                print(id, *item)

def input_path():
    path = input('Введите имя файла: ')
    return path

def input_contact():
    name_contact = input('Введите имя: ')
    phone_contact = input('Введите номер телефона: ')
    comment_contact = input('Введите комментарий: ')
    return (name_contact, phone_contact, comment_contact)

def input_change():
    id = int(input('Введите номер контакта: '))
    print('Что изменить? ')
    choise = input('0 - ФИО, 1 - Телефон, 3 - Комментарий, 4 - Отменить ')
    value = input('Введите изменения: ')
    return(id, choise, value)

def delete_contact():
    id = int(input('Введите номер контакта: '))
    return id

def find_contact():
    char = input('Введите критерий поиска: ')
    return char

