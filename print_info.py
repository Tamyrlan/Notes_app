from os import path

def print_csv():
    file = 'Note.csv'
    if path.exists(file):
        with open(file,'r',encoding='utf-8') as text:
            text_csv = text.readline()
            for i, v in enumerate(text_csv):
                print(v.strip())
    else:
        print('\n Файл с заметками отсутствует')
        return