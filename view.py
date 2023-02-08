def show_menu() -> int:
    print("\n Выберите:\n"
          "1. Показать всю телефонную книгу\n"
          "2. Найти контакт по имени \n"
          "3. Найти контакт по номеру телефона\n"
          "4. Добавить контакт\n"
          "5. Экспортировать справочник в текстовом формате\n"
          "6. Выйти из меню ")

    answer = int(input())
    return answer

def result(data: list):
    for el in data:
        s = ''
        for v, k in el.items():
            s += f'{v}: {k}/n'
        print(s)

def search_name():
    return input("Какую фамилию ищем? ")

def search_number():
    return input("По какому номеру ищем?")

def new_user():
    first_name = input("Имя: ")
    last_name = input("Фамилия: ")
    phone_number = input("Телефонный номер: ")
    comment = input("Комментарий к контакту: ")
    return f'{first_name}, {last_name}, {phone_number}, {comment}'

def file_name():
    return input("Назовите файл для сохранения: ")

