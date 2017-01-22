import sqlite3
conn=sqlite3.connect("new.db")
c=conn.cursor()
c.execute("INSERT INTO Population VALUES('New York', 'NY', 84000)")
c.execute("INSERT INTO Population VALUES('San Francisco', 'CA', 90000)")
conn.commit()
conn.close()