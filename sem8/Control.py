from gettext import find
from importlib.resources import path
import View
import Model


def start():
    choise = 1
    while choise != 9:
        choise = View.show_menu()
        match(choise):
            case 1:
                phone_book = Model.get_phone_book()
                View.show_phone_book(phone_book)
            case 2:
                path = View.input_path()
                Model.set_path(path)
                Model.open_file()
            case 3:
                Model.write_file()
            case 4:
                contact = View.input_contact()
                Model.new_contact(contact)
            case 5:
                contact = View.input_change()
                Model.change_contact(*contact)
            case 6:
                phone_book = View.delete_contact()
                Model.delete_contact(phone_book)
            case 7:
                find = View.find_contact()
                Model.find_contact(find)
