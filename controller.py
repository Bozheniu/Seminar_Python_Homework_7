from view import (show_menu, result, search_name, search_number, new_user, file_name)
from modul import create_txt, create_csv, read_csv, find_name, find_number, add_user

def phonebook():
    answer = show_menu()
    phone_book = read_csv('phonebook.csv')

    while (answer != 6):
        if answer == 1:
            result(phone_book)
        elif answer == 2:
            name = search_name()
            print(find_name(phone_book, name))
        elif answer == 3:
            number = search_number()
            print(find_number(phone_book, number))
        elif answer == 4:
            user_data = new_user()
            add_user(phone_book, user_data)
            create_csv('phonebook.csv', phone_book)
        elif answer == 5:
            is_file_name = file_name()
            create_txt(is_file_name, phone_book)
        answer = show_menu()

