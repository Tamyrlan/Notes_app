from exeptions import data_search
import os

def search():
    search = data_search()
    file = 'Note.csv'
    if os.path.exists(file):
        with open(file,'r',encoding='utf-8') as text:
            count = False
            text_csv = text.readlines()
            for i, v in enumerate(text_csv):
                if search in v:
                    print(v.strip())
                    count = True
                if not count:
                    print('\n Таких данных нет')
                    return False
    else:
        print('\n Файл с заметками отсутсвтует')
        return False