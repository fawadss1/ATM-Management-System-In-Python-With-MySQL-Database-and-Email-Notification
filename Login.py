from DB_Connection import db

print("\n\n HERE IS LOGIN!\n")
Chances = 2
while True:
    User_Name = input(" Enter Your User Name : ").lower()
    PIN_Confirmlg = input(" Enter Your 4 Digits PIN Code : ").lower()
    f = db.cursor()
    f.execute("SELECT * FROM `userinfo` WHERE username='" + User_Name + "' AND pin='" + PIN_Confirmlg + "'")
    f.fetchall()
    if f.rowcount > 0:
        print("Congratulations! Login Sucessfull")
        break
    else:
        print("\nInvalid UserName Or PIN Try Again & You Have " + str(Chances) + " More Chances Remained\n")
        Chances -= 1
    if Chances < 0:
        print("Sorry! Your Account has been Blocked Temporary")
        break
