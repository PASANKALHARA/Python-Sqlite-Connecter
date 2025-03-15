import sqlite3
import datetime
import matplotlib.pyplot as plt

conn = sqlite3.connect('tutorial.db')
c = conn.cursor()

def garph_data():
    c.execute('SELECT * FROM stuffToPol')
    dates = []
    values = []
    for row in c.fetchall():
        dates.append(datetime.datetime.fromtimestamp(row[0]))
        values.append(row[1])
    plt.plot_date(dates, values ,'-')
    plt.show()


garph_data()
c.close()
conn.close()