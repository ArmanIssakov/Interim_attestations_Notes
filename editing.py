from search import search
from exceptions import data_editing
import datetime
import inline



def editing():
        date_note = datetime.datetime.now().strftime("%d-%m-%Y,%H:%M:%S")
        if search() == False:
            print('Данные для редактирования отсутствуют')
            return
        else:
            edit_key = data_editing()
            flag = False
        with open('Note.csv', 'r', encoding='utf-8') as note:
            old_data = note.readlines()
        with open('Note.csv', 'w', encoding='utf-8') as note:
            for i, line in enumerate(old_data):
                if line.split(';')[0] != edit_key:
                    note.write(line)
                else: 
                    flag = True
                    print('{}'.format(line))
                    
                     
                    line_array=[]
                    line_array=line.split(';') 
                    super_input = inline.input
                    what_edit =int(input('Что хотите изменить? (1 - название, 2 - содержание)'))
                    if  what_edit == 1:
                        note_name = super_input("Новое название: ", inp=line_array[1])
                        note.write('{};{};{};{}\n'.format(edit_key,note_name,line_array[2],date_note))
                        print('\nНазвание заметки №{} успешно изменено'.format(edit_key))
                        
                    elif what_edit == 2: 
                        note_body = super_input("Новое название: ", inp=line_array[2])
                        note.write('{};{};{};{}\n'.format(edit_key,line_array[1],note_body,date_note))
                        print('\nСодержание заметки №{} успешно изменено'.format(edit_key))
                    else:
                        print('Ошибка ввода')
                        return

        if flag == False:
            print('\nЗаметки под №{} несуществует'.format(edit_key))  
    # search()
    # editing_key = data_editing()
    # # flag = False
    # with open('Note.csv', 'r', encoding='utf-8') as note:
    #     old_data = note.readlines()
    # with open('Note.csv', 'w', encoding='utf-8') as note:
    #     for i, line in enumerate(old_data):
    #         if line.split(';')[0] != editing_key:
    #             note.write(line)
    #         else:
    #             print('{}'.format(line))

    #             print('Что хотите изменить? (1 - название, 2 - содержание)')
                # to_add = []
                # print("\nРедактирование заметки №{}n".format(editing_key))
                # to_add.append(input('Введите новое название: '))
                # to_add.append(input('Введите новое содержание: '))
                # dateNote = datetime.datetime.now().strftime("%d-%m-%Y,%H:%M:%S")
                # # save = input('Сохранить данную заметку? (1 - да, 2 - нет): ')
                # note.write('{};{};{};{}\n'.format(editing_key, to_add[0], to_add[1], dateNote))
    #             flag = True
    # if flag == True:
    #     print('\nЗаметка №{} успешно удалена'.format(edit_key))
    # else:
    #     print('\nЗаметки под №{} несуществует'.format(edit_key))       
# from exceptions import data_editing

# with open ('Note.csv', 'r') as note:
#   old_data = note.readlines()
#   for i in old_data:

# new_data = old_data.replace('что_меняем', 'на_что_меняем')
# with open ('Note.txt', 'w') as note:
#   note.write(new_data)