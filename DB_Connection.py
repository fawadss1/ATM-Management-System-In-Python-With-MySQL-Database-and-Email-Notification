import mysql.connector as mysql

Database_Name = "atm"

chk_db = mysql.connect(
    host="127.0.0.1",
    user="root",
    password=""
)
f = chk_db.cursor()
f.execute("SHOW DATABASES")
DB = f.fetchall()
if (Database_Name,) in DB:
    pass
else:
    f.execute("CREATE DATABASE " + Database_Name)
Database = Database_Name

db = mysql.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database=Database
)
