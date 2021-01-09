from DB_Connection import db
from Narrator import Narrator

def forgot_Pin():
    global User_Namedb, PIN_Confirm
    Narrator("if You Forgot Your PIN Code Press 1 : ")
    opt = input()
    print("*" + "---" * 15 + "*")
    if opt == "1":
        while True:
            Narrator("Please Enter Ur Username OR Email Address : ")
            username_rc = input()
            f = db.cursor()
            f.execute("SELECT * FROM `userinfo` WHERE username='" + username_rc + "' or email='" + username_rc + "'")
            fd = f.fetchall()
            if f.rowcount > 0:
                for i in fd:
                    User_Namedb = i[4]
                    PIN_Confirm = i[5]
                print("*" + "---" * 15 + "*")
                Narrator("Your Username is : " + User_Namedb)
                Narrator("Your PIN Code is : " + str(PIN_Confirm))
                Narrator("Please Press (Shift+F10) To Login To Your Account Again")
                print("*" + "---" * 15 + "*")
                break
            else:
                Narrator("Sorry Your Enter UserName Not Found Try Again ")
                print("*" + "---" * 15 + "*")
    else:
        Narrator("Invalid Key System is not Responding Please Press (Shift+F10) To Refresh")
        print("*" + "---" * 23 + "*")