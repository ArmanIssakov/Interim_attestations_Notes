from search import search
from print_info import print_csv
from exceptions import user_choice
from delete import delete
from add_info import adding
from editing import editing



def input_contact_menu_choice():
   
    print()
    print('-----------------------')
    print('Работа с заметками')
    print('-----------------------')
    print('1. Создать новую заметку')
    print('2. Список заметок')
    print('3. Поск заметки')
    print('4. Изменить существующую заметку')
    print('5. Удалить заметку')
    print('-----------------------')
    print('0. Выход')
    choice_menu = user_choice()
    if choice_menu == 1:
        adding()
        return submenu()
    elif choice_menu == 2:
        print('\nВсе заметки\n')
        print_csv()
        return submenu()
    elif choice_menu == 3:
        search()
        return submenu()
    elif choice_menu == 4:  #добавить
        editing()
        return submenu()
    elif choice_menu == 5:  
        delete()
        return submenu()

    elif choice_menu == 0:
        return exit()
    else:
        print('Такого пункта нет в меню')
        return input_contact_menu_choice()

def submenu():
    input_num = int(input('\nПродолжить работу с заметками? (1 - да, 2 - нет): '))
    if input_num == 1:
        return input_contact_menu_choice()
    elif input_num == 2:
        return exit() 
    else:
        print('Ошибка ввода')
        return submenu()

