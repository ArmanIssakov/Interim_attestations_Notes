from exceptions import data_delete
from search import search


def delete():  # удаление заметки
    if search() == False:
        print('Данные для удаления отсутствуют')
        return
    else:
        del_key = data_delete()
        flag = False
        with open('Note.csv', 'r', encoding='utf-8') as note:
            old_data = note.readlines()
        with open('Note.csv', 'w', encoding='utf-8') as note:
            for i, line in enumerate(old_data):
                if line.split(';')[0] != del_key:
                    note.write(line)
                else:
                    flag = True
                    try:
                        input_del = int(input(
                            'Вы действительно хотите удалить заметку №{}\n{}\n(1 - да, 2 - нет): '.format(del_key, line)))
                        if input_del == 1:
                            print('\nЗаметка №{} успешно удалена'.format(del_key))
                        elif input_del == 2:
                            note.write(line)
                    except ValueError:
                        print('Ошибка ввода')
                        return
        if flag == False:
            print('\nЗаметки под №{} несуществует'.format(del_key))
