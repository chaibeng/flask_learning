import sqlite3

conn = sqlite3.connect('database.db')
cur = conn.cursor()

# execute a SELECT statement
cur.execute('SELECT * FROM students')

# fetch the results
rows = cur.fetchall()

# print the results
for row in rows:
    print(row)

# close the connection
conn.close()
