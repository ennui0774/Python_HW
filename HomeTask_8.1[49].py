# 8.1[49]: Создать телефонный справочник с возможностью импорта и экспорта данных в формате csv. Доделать задание вебинара и реализовать Update, Delete
# Информация о человеке: Фамилия, Имя, Телефон, Описание
# Корректность и уникальность данных не обязательны.
# Функционал программы
# 1) телефонный справочник хранится в памяти в процессе выполнения кода.
# Выберите наиболее удобную структуру данных для хранения справочника.
# 2) CRUD: Create, Read, Update, Delete
# Create: Создание новой записи в справочнике: ввод всех полей новой записи, занесение ее в справочник.
# Read: он же Select. Выбор записей, удовлетворяющих заданном фильтру: по первой части фамилии человека.
#  Берем первое совпадение по фамилии.
# Update: Изменение полей выбранной записи. Выбор записи как и в Read, заполнение новыми значениями.
# Delete: Удаление записи из справочника. Выбор - как в Read.
# 3) экспорт данных в текстовый файл формата csv

# 4) импорт данных из текстового файла формата csv

# Используйте функции для реализации значимых действий в программе

def main_menu(sprav):
    while True:
        user_choice = input('1 - Найти контакт\n'
                            '2 - Добавить контакт\n'
                            '3 - Изменить контакт\n'
                            '4 - Удалить контакт\n'
                            '5 - Показать весь справочник\n\n'
                            '0 - EXIT\n')
        print()
        if user_choice == '1':
            lst_contacts = read_file(file)
            search_param, what = ask_search()
            res = search_contact(lst_contacts, search_param, what)
            print(res)
        elif user_choice == '2':
            add_contact(sprav)
        elif user_choice == '3':
            change_contact(sprav)
        elif user_choice == '4':
            delete_contact(sprav)
        elif user_choice == '5':
            show(sprav)
        elif user_choice == '0':
            print('До свидания!')
            break


def read_file(file):
    with open(file, 'r', encoding='utf-8') as fd:
        lines = fd.readlines()
    headers = ['Фамилия', 'Имя', 'Номер телефона']
    list_contacts = []
    for line in lines:
        line = line.strip().split()
        list_contacts.append(dict(zip(headers, line)))
    return list_contacts


def read_file_to_list(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        contact_list = []
        for line in file.readlines():
            contact_list.append(line.split())
    return contact_list


def ask_search():
    print('По какому полю выполнить поиск?')
    param = input('1 - по фамилии\n2 - по имени\n3 - по номеру телефона\n')
    print()
    what = None
    if param == '1':
        what = input('Введите фамилию для поиска: ')
        print()
    elif param == '2':
        what = input('Введите имя для поиска: ')
        print()
    elif param == '3':
        what = input('Введите номер для поиска: ')
        print()
    return param, what


def search_contact(list_contacts: list, param: str, what: str):
    param_dict = {'1': 'Фамилия', '2': 'Имя', '3': 'Номер телефона'}
    found_contacts = []
    for contact in list_contacts:
        if contact[param_dict[param]] == what:
            found_contacts.append(contact)
    return found_contacts


def find_contact(contact_list):
    search_field, search_value = ask_search()
    search_value_dict = {'1': 'Фамилия', '2': 'Имя', '3': 'Номер телефона'}
    found_contacts = []
    for contact in contact_list:
        if contact[search_value_dict[search_field]] == search_value:
            found_contacts.append(contact)
    return found_contacts


def ask_user():
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    phone_number = input('Введите номер телефона: ')
    return last_name, first_name, phone_number


def add_contact(file_name):
    data_str = ' '.join(ask_user())
    with open(file_name, 'a', encoding='utf-8') as file:
        file.write(f'{data_str}\n')


def show(file_name):
    list_of_contacts = sorted(read_file(file_name), key=lambda x: x['Фамилия'])
    print_contacts(list_of_contacts)
    print()
    return list_of_contacts


def search_to_modify(contact_list: list):
    search_field, search_value = ask_search()
    search_result = []
    for contact in contact_list:
        if contact[int(search_field) - 1] == search_value:
            search_result.append(contact)
    if len(search_result) == 1:
        return search_result[0]
    elif len(search_result) > 1:
        print('Найдено несколько контактов')
        for i in range(len(search_result)):
            print(f'{i + 1} - {search_result[i]}')
        num_count = int(
            input('Выберите номер контакта, который нужно изменить/удалить: '))
        return search_result[num_count - 1]
    else:
        print('Контакт не найден')
    print()


def change_contact(file_name):
    contact_list = read_file_to_list(file_name)
    number_to_change = search_to_modify(contact_list)
    contact_list.remove(number_to_change)
    print('Какое поле вы хотите изменить?')
    field = input('1 - Фамилия\n2 - Имя\n3 - Номер телефона\n')
    if field == '1':
        number_to_change[0] = input('Введите фамилию: ')
    elif field == '2':
        number_to_change[1] = input('Введите имя: ')
    elif field == '3':
        number_to_change[2] = input('Введите номер телефона: ')
    contact_list.append(number_to_change)
    with open(file_name, 'w', encoding='utf-8') as file:
        for contact in contact_list:
            line = ' '.join(contact) + '\n'
            file.write(line)


def delete_contact(file_name):
    contact_list = read_file_to_list(file_name)
    number_to_change = search_to_modify(contact_list)
    contact_list.remove(number_to_change)
    with open(file_name, 'w', encoding='utf-8') as file:
        for contact in contact_list:
            line = ' '.join(contact) + '\n'
            file.write(line)


def print_contacts(contact_list: list):
    for contact in contact_list:
        for key, value in contact.items():
            print(f'{key}: {value:12}', end='')
        print()


if __name__ == '__main__':
    file = 'file.txt'
    main_menu(file)