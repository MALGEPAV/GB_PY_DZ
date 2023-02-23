import operations as op


def input_data():

    print("""
    Введите данные.
    Если какое-то поле не важно, введите пустую строку, 
    Все введенные пробелы будут удалены.
    """)

    last_name = input('Введите фамилию: ').upper().replace(' ', '')
    first_name = input('Введите имя: ').upper().replace(' ', '')
    middle_name = input('Введите отчество: ').upper().replace(' ', '')
    phone_number = input('Введите номер телефона: ').upper().replace(' ', '')

    return [last_name, first_name, middle_name, phone_number]


def main_menu():
    operation = ''
    while (operation != '0'):
        print("""
        ГЛАВНОЕ МЕНЮ

        '1': вывод ВСЕХ контактов на экран
        '2': ввод данных для поиска, удаления, и изменения контактов 
        '3': удалить ВСЕ контакты
        '0': завершение работы
        """)

        operation = input('Ввод: ').strip()
        while operation not in ('1', '2', '3', '0'):
            print('Некорректный ввод, попробуйте еще раз:')
            operation = input('Ввод: ').strip()

        if operation == '1':
            op.print_all()
        elif operation == '2':
            data = input_data()
            list_of_matching_records = op.find_matching_records(data)
            if list_of_matching_records:
                matching_records_menu(list_of_matching_records)
            else:
                no_matching_records_menu(data)
        elif operation == '3':
            op.delete_all()
        else:
            print('\nЗАВЕРШЕНИЕ РАБОТЫ')


def matching_records_menu(list_of_matching_records):
    print('\nПодходящие имеющиеся записи:\n')
    for (i, record_list) in enumerate(list_of_matching_records):
        print(f'{i+1}. ' + ' '.join(record_list))

    print("""
    Действия:
        '1': выбрать контакт из списка 
        '2': удалить ВСЕ найденные контакты
        '0': главное меню
        """)

    operation = input('Ввод: ').strip()
    while operation not in ('1', '2', '0'):
        print('Некорректный ввод, попробуйте еще раз:')
        operation = input('Ввод: ').strip()

    if operation == '1':
        index = input('Введите номер контакта из списка:').strip()
        while index not in [str(i+1) for i in range(len(list_of_matching_records))]:
            print('Некорректный ввод, попробуйте еще раз:')
            index = input('Ввод: ').strip()
        selected_record = list_of_matching_records[int(index)-1]
        record_menu(selected_record)
    elif operation == '2':
        op.delete_matching_records(list_of_matching_records)
        print('Контакты успешно удалены')


def no_matching_records_menu(input_data):
    print('\nПодходящих записей нет...')
    print("""
    Действия:
        '1': добавить такой контакт 
        '0': главное меню
        """)
    operation = input('Ввод: ').strip()
    while operation not in ('1', '0'):
        print('Некорректный ввод, попробуйте еще раз:')
        operation = input('Ввод: ').strip()

    if operation == '1':
        op.add_record(input_data)
        print('\nКонтакт '+' '.join(list(map(lambda x: x if x else '???',
              input_data)))+' успешно схранен')


def record_menu(selected_record):
    print('\nРабота с контактом: '+' '.join(selected_record))
    print("""
    Действия:
        '1': изменить контакт 
        '2': удалить контакт
        '0': главное меню
        """)

    operation = input('Ввод: ').strip()
    while operation not in ('1', '2', '0'):
        print('Некорректный ввод, попробуйте еще раз:')
        operation = input('Ввод: ').strip()

    if operation == '1':
        print('\nВведите новые данные контакта:')
        new_data = input_data()
        op.modify_record(selected_record, new_data)
    elif operation == '2':
        op.delete_matching_records([selected_record])
        print('Контакт успешно удален')
