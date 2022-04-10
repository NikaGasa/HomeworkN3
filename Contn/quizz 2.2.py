import sqlite3
connect = sqlite3.connect('morty.db')
cursor = connect.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Dog
                (name VARCHAR,
                 color VARCHAR,
                 age INT);''')

cursor.execute("INSERT INTO Dog (name, color, age) VALUES ('Kiki', 'gray', 3)")
connect.commit()
cursor.execute("SELECT * FROM Dog")
print(cursor.fetchone())