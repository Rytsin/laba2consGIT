import sqlite3

def connect_db(name_db):
    db = sqlite3.connect(name_db)
    return db

def menu(db):
    cursor=db.cursor()
    print('показать таблицу "1"')
    print('добавить записи  "2"')
    print('удалить cтроку   "3"')
    print('обновить ячейку  "4"')
    print('заверешние программы "5"')
    n = input('введите команду-->:')
    if n == '1':
        show_table(db)
        
    elif n == '2':
        add(db)
        db.commit
        print('вы выбрали команду-->',n)
    elif n == '3':
        delete(db)
        db.commit
        print('вы выбрали команду-->',n)
    elif n == '4':
        #update
        print('вы выбрали команду-->',n)
    elif n == '5':
        #end
        print('вы выбрали команду-->',n)
        exit()
    else:
        print('неверный ввод,попробуйте ввести еще раз')
    menu(db)  
        
def show_table(db):
    cursor=db.cursor()
    cursor.execute("select * from garage")
    table = cursor.fetchall()
    for el in table:
        print("|"+el[0]+"|"+el[1]+"|"+el[2]+"|"+el[3]+"|"+el[4]+"|")
def add(db):
    cursor=db.cursor()
    db.commit()


def delete(db):
    cursor=db.cursor()
    cursor.execute("delete from garage where rowid==1")
    db.commit               
    
    
    
    
    
    
name_db = input('введите название базы данных, к которой хотите подключиться:')
db = connect_db(name_db)
print('вы подключились к базе данных:',name_db)

menu(db)








    
    
    
    