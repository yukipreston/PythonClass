import sqlite3

conn = sqlite3.connect('ages.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Ages')
cur.execute('''
CREATE TABLE Ages (name VARCHAR(128), age INTEGER)''')

cur.execute('DELETE FROM Ages;')
cur.execute('INSERT INTO Ages (name, age) VALUES (?, ?)', ('Mathilda', 14));
cur.execute('INSERT INTO Ages (name, age) VALUES (?, ?)', ('Anayah', 26));
cur.execute('INSERT INTO Ages (name, age) VALUES (?, ?)', ('Samiha', 29));
cur.execute('INSERT INTO Ages (name, age) VALUES (?, ?)', ('Chu', 32));
cur.execute('INSERT INTO Ages (name, age) VALUES (?, ?)', ('Kaeden', 26));

conn.commit()

cur.execute('SELECT hex(name || age) AS X FROM Ages ORDER BY X')
for row in cur:
    print(row)
    
cur.close()
