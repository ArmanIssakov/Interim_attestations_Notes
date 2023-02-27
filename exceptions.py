def user_choice():
    try:
        choice = int(input('\nВыберите пункт меню: '))
        return choice
    except ValueError:
        print('Ошибка ввода')


def data_search():
    try:
        search = input('\nВведите данные  для поска заметки: ')
        return search
    except ValueError:
        print('Ошибка ввода')


def data_delete():
    try:
        delete = input('\nВведите номер записи, для удаления: ')
        return delete
    except ValueError:
        print('Ошибка ввода')


def data_editing():
    try:
        editing = input('\nВведите номер записи, для изменения: ')
        return editing
    except ValueError:
        print('Ошибка ввода')