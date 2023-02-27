def writing_scv(): #создание файла для заметок
    with open('Note.csv', 'a', encoding='utf-8') as data:
        data.write('№;Название;Содержание заметки;Дата создания/изменения\n')