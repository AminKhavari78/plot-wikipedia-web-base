import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (name, search) VALUES (?, ?)",
            ('First Post', 'Content for the first post')
            )


connection.commit()
connection.close()