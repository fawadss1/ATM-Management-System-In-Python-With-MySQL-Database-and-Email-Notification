welcome_message = lambda: print("Congratulations! Regestration has been Completed Sucsessfully")

print("\t" * 14 + "*" + "--" * 27 + "*")
print("\t" * 14 + "| Most Strongly Welcome to Fawad ATM Management System |")
print("\t" * 14 + "*" + "--" * 27 + "*")
try:
    from DB_Connection import db

    Name = input("\nEnter Your Name : ").capitalize()
    F_Name = input("\nEnter Your Father Name : ").capitalize()
    print("\nEnter Your Date Of Birth")
    try:
        DD = int(input("Day : "))
        MM = int(input("Month : "))
        YYY = int(input("Year : "))
        if 1 <= DD <= 31 and 1 <= MM <= 12 and 1947 <= YYY <= 2000:
            DOB = "0" + str(DD) + "/0" + str(MM) + "/" + str(YYY)
            Total_Amount = int(input("Enter Your Money Amount (100-100000) : "))
            while Total_Amount < 100 or Total_Amount > 100000:
                Total_Amount = int(input("Invalid Range Enter Your Money Amount Again (100-100000) : "))
            User_Name = input("\nEnter Your User Name : ").lower()
            PIN = input("\nEnter Your 4 Digits PIN : ").lower()
            if len(PIN) == 4:
                pass
            else:
                while len(PIN) != 4:
                    print("Invalid Your PIN Code Must Be 4 Digits Only\n")
                    PIN = input("Enter Your 4 Digits PIN : ")
            PIN_Confirm = input("Enter Your 4 Digits PIN Again : ")
            if PIN == PIN_Confirm:
                pass
            else:
                while PIN != PIN_Confirm:
                    print("\nSorry Your PIN Does not Match Try Again")
                    PIN_Confrm = input("Enter Your 4 Digits PIN Again : ")
            f = db.cursor()
            f.execute("SHOW TABLES")
            tbl = f.fetchall()
            if ("userinfo",) in tbl:
                pass
            else:
                f.execute("CREATE TABLE `userinfo` (id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(255),father_name VARCHAR(255),dob VARCHAR(255),username VARCHAR(255),pin VARCHAR(11),amount INT)")
            f.execute("SELECT * FROM `userinfo` WHERE username= '" + User_Name + "'")
            f.fetchall()
            if f.rowcount > 0:
                print("\nThis User Name is Already Registered Please Login To Your Account")
            else:
                f.execute("INSERT INTO `userinfo` (name,father_name,dob,username,pin,amount) VALUES ('" + Name + "','" + F_Name + "','" + DOB + "','" + User_Name + "','" + PIN_Confirm + "','" + str(Total_Amount) + "')")
                db.commit()
                welcome_message()
        else:
            print("Invalid Values Or You Are Under Age Thank You")
    except ValueError:
        print("|" + "**" * 54 + "|")
        print("|\t\t\t\t\tInvalid Values System is not Responding Please Press (Shift+F10) To Refresh" + "  " * 7 + "|")
        print("|" + "**" * 54 + "|")
except:
    print("\n" + "|" + "**" * 38 + "|")
    print("|\t\t\t\tYour DataBase Server is Down! Please Try Again" + " " * 15 + "|")
    print("|" + "**" * 38 + "|")
