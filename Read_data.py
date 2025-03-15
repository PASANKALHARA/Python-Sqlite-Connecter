import sqlite3

conn = sqlite3.connect('tutorial.db')
c = conn.cursor()

def read_data_enrty():
    c.execute('SELECT * FROM stuffToPol')
    for row in c.fetchall():
        print(row)


read_data_enrty()
c.close()
conn.close()