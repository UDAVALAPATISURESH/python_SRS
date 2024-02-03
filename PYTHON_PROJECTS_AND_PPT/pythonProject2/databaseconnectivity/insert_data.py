import sqlite3
connecton = sqlite3.connect("database1.db")

crsr = connecton.cursor()

sql_commandn = """INSERT INTO emp ( VALUES (10,"suresh","s","h");"""

crsr .execute(sql_commandn)

connecton.commit()
connecton.close()