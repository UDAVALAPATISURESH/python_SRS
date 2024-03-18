import sqlite3

# connecting to  the database
connecton = sqlite3.connect("database1.db")

# cursor

crsr = connecton.cursor()

# SQL command to create a table in the database
sql_command = """CREATE TABLE enp (
staff_number INTEGER PRIMARY KEY ,
fname VARCHAR(20),
lname VARCHAR(30),
gender CHAR (1),
joining DATE );"""

# execute the statement
crsr.execute(sql_command)

# closs the connection

connecton.close()

