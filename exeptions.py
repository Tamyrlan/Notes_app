def user_choice():
    try:
        choice = int(input('\nВыберите пункт меню:'))
        return choice
    except ValueError:
        print('Ошибка ввода')

def data_search():
    try:
        search = input('\n Введите данные для поиска заметки:')
        return search
    except ValueError:
        print('Ошибка ввода')

def data_delete():
    try:
        search = input('\n Введите номер записи, для удаления:')
        return search
    except ValueError:
        print('Ошибка ввода')
    
def data_editting():
    try:
        search = input('\n Введите номер записи, для изменения:')
        return search
    except ValueError:
        print('Ошибка ввода')