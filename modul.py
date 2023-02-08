def find_name(data, last_name):
    for el in data:
        if el.get("Фамилия") == last_name:
            return el.get("Телефон")
        return "Контакт не найден"

def find_number(data, phone_number):
    for el in data:
        if el.get("Телефон") == phone_number:
            return f'{el.get("Фамилия")}, {el.get("Имя")}'
        return "Контакт не найден"

def add_user(data, user_data):
    fields = ['Имя', 'Фамилия', 'Телефон', 'Комментарий']
    record = dict(zip(fields, user_data.split(',')))
    data.append(record)
    return "Контакт добавлен"

def create_txt(filename: str, data: list):
    with open(filename, 'w', encoding='utf-8') as fout:

        for i in range(len(data)):
            s = ''
            for v in data[i].values():
                s += v + ','
            fout.write(f'{s[:-1]}')

def create_csv(filename: str, data: list):
    with open(filename, 'w', encoding='utf-8') as fout:
        for i in range(len(data)):
            s = ''
            for v in data[i].values():
                s += v + ','
                fout.write(f'{s[:-1]}')

def read_csv(filename: str) -> list:
    data = []
    fields = ['Имя', 'Фамилия', 'Телефон', 'Комментарий']
    with open(filename, 'r', encoding='utf-8') as fin:
        for line in fin:
            record = dict(zip(fields, line.strip().split(',')))
            data.append(record)

    return data

