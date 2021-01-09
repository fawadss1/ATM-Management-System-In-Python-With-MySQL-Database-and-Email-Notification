from Narrator import Narrator
from Forgot_PIN import forgot_Pin

try:
    from DB_Connection import db

    Narrator(" \nPlease Login To Your Account!")
    Chances = 0
    while True:
        print("*" + "---" * 15 + "*")
        Narrator(" Enter Your User Name : ")
        User_Name = input().lower()
        print("*" + "---" * 15 + "*")
        Narrator(" Enter Your 4 Digits PIN Code : ")
        PIN_Confirmlg = input().lower()
        print("*" + "---" * 15 + "*")
        f = db.cursor()
        f.execute("SELECT * FROM `userinfo` WHERE username='" + User_Name + "' AND pin='" + PIN_Confirmlg + "'")
        f.fetchall()
        if f.rowcount > 0:
            Narrator("Congratulations! Login Successful")
            print("*" + "---" * 15 + "*")
            break
        else:
            print("*" + "---" * 23 + "*")
            Narrator("Invalid UserName Or PIN Try Again & You Have " + str(Chances) + " More Chances Remained")
            print("*" + "---" * 23 + "*")
            Chances -= 1
        if Chances < 0:
            Narrator("Sorry! Your Account has been Blocked Temporary Due to Wrong Pin Entry")
            print("*" + "---" * 23 + "*")
            forgot_Pin()
            break
except:
    print("\n" + "|" + "**" * 38 + "|")
    Narrator("|\t\t\t\tYour DataBase Server is Down! Please Try Again" + " " * 15 + "|")
    print("|" + "**" * 38 + "|")
