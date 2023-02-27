import file_writing
import datetime
import os



def adding():
    if not os.path.exists('Note.csv'):
        file_writing.writing_scv()
    if not os.path.exists('last_key.txt'):
        file_writing.last_key_txt()
    to_add = []
    print("\nСоздание новой заметки\n")
    to_add.append(input('Название: '))
    to_add.append(input('Содержание: '))
    date_note = datetime.datetime.now().strftime("%d-%m-%Y,%H:%M:%S")
    save = input('Сохранить данную заметку? (1 - да, 2 - нет): ')
    if save == '1':
        with open('last_key.txt', "r") as my_f:
            last_key = my_f.readline().split()
            new_key = int(last_key[-1])
        with open('Note.csv', "a", encoding='utf-8') as base:
            base.write('{};{};{};{}\n'.format(new_key + 1, to_add[0], to_add[1], date_note))
        with open('last_key.txt', "w", encoding='utf-8') as my_f:
            my_f.write(f"last_key = {new_key + 1}")
        print('данные сохранены')
        return to_add
    elif save == '2':
        print('Данная заметка не сохранена')
    else:
        print('Ошибка ввода')
        

