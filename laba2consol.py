import sqlite3
db= sqlite3.connect('laba2cons.db')
cursor=db.cursor()
'''cursor.execute("""create table garage (
zavod text,
marka text,
color text,
type transm text,
engine text
)""")'''
#cursor.execute("insert into articles values ()")
#cursor.execute("delete from articles")
#cursor.execute("update articles set avtor='AvtoR'") 
#cursor.execute("select * from articles")
#print(cursor.fetchmany(2))
#items=cursor.fetchall()
#print(cursor.fetchone()[1])


db.commit()




db.close
