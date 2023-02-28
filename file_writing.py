def writing_scv():
    with open('Note.csv','a',encoding='utf-8') as data:
        data.write('№;Название;Содержание заметки;Дата создания/изменения\n')

def last_key():
    with open('last_key.txt',"r") as my_f:
        last_key = my_f.readline().split()
        new_key = int(last_key[-1])
        with open('last_key.txt','w',encoding='utf-8') as my_f:
            my_f.write(f"last_key = {new_key + 1}")
        return new_key + 1

def last_key_txt():
    with open('last_key.txt','a',encoding='utf-8') as data:
        data.write('last_key = 0')
