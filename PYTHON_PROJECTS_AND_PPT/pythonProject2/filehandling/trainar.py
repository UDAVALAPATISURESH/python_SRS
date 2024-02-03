# def file_read():
#     file = open(r"C:\Users\sisek\PycharmProjects\pythonProject\file handling\example1.txt", "w")
#     content = file.read()
#     file.close()
#     return content
#
#
# # cont = file_read()
# # print(cont)
#
# # file = open(r"C:\Users\sisek\PycharmProjects\pythonProject\file handling\example.txt", "r")
# # content = file.read()
# # print(content)
# # file.close()
#
# # with open("example.txt", "r") as file:
# #     content = file.read()
#
# file = open(r"C:\Users\sisek\PycharmProjects\pythonProject\file handling\example1.txt", "a")
# content = file.write("\n Africa")
# print(content)




import sqlite3

# connecting to the database
connection = sqlite3.connect("database1.db")

# cursor
crsr = connection.cursor()

# SQL command to create a table in the database
sql_command = """CREATE TABLE emp (
staff_number INTEGER PRIMARY KEY,
fname VARCHAR(20),
lname VARCHAR(30),
gender CHAR(1),
joining DATE);"""

# execute the statement
crsr.execute(sql_command)

# close the connection
connection.close()
