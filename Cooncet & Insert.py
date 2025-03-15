import sqlite3

conn = sqlite3.connect('tutorial.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS stuffToPol(unix REAL,datestamp TEXT,keyword TEXT, value  READ )')

def data_entry():
    c.execute("INSERT INTO stuffToPol VALUES(1451255551,'2016-01-02','Python',8)")
    conn.commit()
    c.close()
    conn.close()

create_table()
data_entry()
