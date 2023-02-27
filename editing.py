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
        try:
            what_edit =int(input('Что хотите изменить? (1 - название, 2 - содержание)'))
            if what_edit != 1 or what_edit != 2:
                print('Ошибка ввода')
                return   
        except ValueError:
            print('Ошибка ввода')
            return 
            

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
                    
                    if  what_edit == 1:
                        note_name = super_input("Новое название: ", inp=line_array[1])
                        note.write('{};{};{};{}\n'.format(edit_key,note_name,line_array[2],date_note))
                        print('\nНазвание заметки №{} успешно изменено'.format(edit_key))
                        
                    elif what_edit == 2: 
                        note_body = super_input("Новое название: ", inp=line_array[2])
                        note.write('{};{};{};{}\n'.format(edit_key,line_array[1],note_body,date_note))
                        print('\nСодержание заметки №{} успешно изменено'.format(edit_key))
                    
        if flag == False:
            print('\nЗаметки под №{} несуществует'.format(edit_key))  
