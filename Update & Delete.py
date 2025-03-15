import sqlite3


conn = sqlite3.connect('tutorial.db')
c = conn.cursor()

def del_and_update():
    c.execute('SELECT * FROM stuffToPol')
    [print(row) for row in c.fetchall()]
############################################# UPDATE CODE #############################################
    '''c.execute('UPDATE stuffToPolt SET value = 99 WHERE value = 8')
    conn.commit()

    c.execute('SELECT * FROM stuffToPol')
    [print(row) for row in c.fetchall()]'''

############################################# DELETE CODE #############################################
    c.execute('DELETE FROM stuffToPolt  WHERE  value =99')
    conn.commit()
    print(50 * '#')
    c.execute('SELECT * FROM stuffToPol')
    [print(row) for row in c.fetchall()]

del_and_update()
c.close()
conn.close()