from os import path


def print_csv(): # печать в консоль из файла Note.csv
    file = 'Note.csv'
    if path.exists(file):
        with open(file, 'r', encoding='utf-8') as text:
            text_csv = text.readlines()
            for i, v in enumerate(text_csv):
                print(v.strip())
    else:
        print('\nФайл с заметками отсутствует')
        return 
