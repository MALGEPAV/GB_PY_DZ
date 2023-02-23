
def print_all():
    if no_records():
        return 1
    with open('contacts.txt', 'r') as c:
        print('\nВСЕ контакты:\n')
        for record in c:
            print(record, end='')


def find_matching_records(search_data):
    actual_search_data = [(i, s) for (i, s) in enumerate(search_data) if s]
    list_of_matching_records = list()
    with open('contacts.txt', 'r') as c:
        c = open('contacts.txt', 'r')
        for record in c:
            record_list = record.split()
            for (i, s) in actual_search_data:
                if record_list[i] != s:
                    break
            else:
                list_of_matching_records.append(record_list)
    return list_of_matching_records


def add_record(new_data):
    new_record = ' '.join(
        list(map(lambda x: x if x else '???', new_data)))+'\n'
    with open('contacts.txt', 'a') as c:
        c.write(new_record)


def delete_all():
    if no_records():
        return 1
    with open('contacts.txt', 'w') as c:
        c.write('')
    print('УДАЛЕНО ВООБЩЕ ВСЕ')


def delete_matching_records(list_of_matching_records):
    with open('contacts.txt', 'r') as c:
        new_content = [record for record in c if record.split()
                       not in list_of_matching_records]
    with open('contacts.txt', 'w') as c:
        c.writelines(new_content)


def modify_record(selected_record, new_data):
    delete_matching_records([selected_record])
    new_actual_data = [(i, s) for (i, s) in enumerate(new_data) if s]
    for (i, s) in new_actual_data:
        selected_record[i] = s
    add_record(selected_record)
    print('\nКонтакт успешно изменен')


def no_records():
    with open('contacts.txt', 'r') as c:
        char = c.read(1)
        if not char:
            print('Список контактов пуст...')
        return not char
