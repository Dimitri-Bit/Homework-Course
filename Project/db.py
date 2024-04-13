import sqlite3

conn = sqlite3.connect("games.db")

cursor = conn.cursor()

# cursor.execute("""CREATE TABLE GAME (id INTEGER PRIMARY KEY, solution TEXT)""")

# cursor.execute("INSERT INTO GAME(id, solution) VALUES(?, ?)", (1, "[123,123,123,12,3]"))

cursor.execute("SELECT * FROM GAME")

games = cursor.fetchall()
print(games)


conn.commit()
conn.close()