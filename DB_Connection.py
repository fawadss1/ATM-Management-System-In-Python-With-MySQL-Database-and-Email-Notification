try:
    import mysql.connector as mysql

    Database = "atm"

    chk_db = mysql.connect(
        host="127.0.0.1",
        user="root",
        password=""
    )
    c_db = chk_db.cursor()
    c_db.execute("CREATE DATABASE IF NOT EXISTS " + Database)
    db = mysql.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database=Database
    )
except:
    print("Sorry! Your DataBase Server is Down! Please Run Your Database Server")
