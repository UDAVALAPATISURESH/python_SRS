import mysql.connector
conn = mysql.connector.connect(host="localhost",user="root",passwd="computer")
c=conn.cursor()
c.execute("show database")
for i in c:
    print(i)