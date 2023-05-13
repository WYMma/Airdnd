import sqlite3

conn = sqlite3.connect('hotels.db')
c = conn.cursor()

# creation des tableaux
'''
c.execute(""" CREATE TABLE hotel1 (
                        roomid INTEGER PRIMARY KEY AUTOINCREMENT,
                        type text,
                        stat text)""")

c.execute(""" CREATE TABLE hotel2 (
                        roomid INTEGER PRIMARY KEY AUTOINCREMENT,
                        type text,
                        stat text)""")

c.execute(""" CREATE TABLE hotel3 (
                        roomid INTEGER PRIMARY KEY AUTOINCREMENT,
                        type text,
                        stat text)""")

c.execute(""" CREATE TABLE hotel4 (
                        roomid INTEGER PRIMARY KEY AUTOINCREMENT,
                        type text,
                        stat text)""")
'''
# remplissage des tableaux
'''
for i in range(50):
    c.execute(""" INSERT INTO hotel4 (type, stat ) VALUES ( 'Single', 'free' )""")
    conn.commit()
conn.close()
'''


