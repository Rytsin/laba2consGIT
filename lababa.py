import sqlite3
db= sqlite3.connect('laba2cons.db')
cursor=db.cursor()
'''cursor.execute("""create table if not exists garage (
zavod text,
marka text,
color text,
transm text,
engine text
    )""")'''

cursor.execute("insert into garage values ('1','2','3','4','5')")
db.commit()
db.close
