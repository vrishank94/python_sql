import sqlite3
with sqlite3.connect("new.db")as connection:
	c=connection.cursor()
	cities=[
	('Boston','MA',50000),
	('Illinois','CH',800000)

	]
	c.executemany('INSERT INTO population VALUES(?,?,?)',cities)
