from Functionality import Functions, Name
import datetime as T

Fun = Functions()
y = T.datetime.now()
ABN = [
    "\t\t\t\t\t\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",
    "\t\t\t\t\t\t|                              Fawad ATM Management System                                 |",
    f"\t\t\t\t\t\t|                            Dear {Name} Most Strongly Welcome                              |",
    "\t\t\t\t\t\t|__________________________________________________________________________________________|",
    "\t\t\t\t\t\t|          (1) Profile                      |          (2) User Credentials                |",
    "\t\t\t\t\t\t|___________________________________________|______________________________________________|",
    "\t\t\t\t\t\t|          (3) Cash Deposit                 |          (4) Cash Withdrawal                 |",
    "\t\t\t\t\t\t|___________________________________________|______________________________________________|",
    "\t\t\t\t\t\t|          (5) Balance Enquiry              |          (6) Receipt                         |",
    "\t\t\t\t\t\t|___________________________________________|______________________________________________|",
    "\t\t\t\t\t\t|          (7) Change PIN                   |          (8) Delete Account                  |",
    "\t\t\t\t\t\t|___________________________________________|______________________________________________|",
    "\t\t\t\t\t\t|          (9)  Logout                      |          " + y.strftime("%d/%m/%Y") + "  " * 13 + "|",
    "\t\t\t\t\t\t|******************************************************************************************|",
    "\t\t\t\t\t\t|mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm|",
    "\t\t\t\t\t\t|                                                                                          |",
    "\t\t\t\t\t\t|_______________________Copyright@ 2020 Fawad. All Rights Reserved______________________v2_|",
    "\t\t\t\t\t\t*~~~~~~~~~~-----------------~~First Pro Python Programm Ever~~-------------------~~~~~~~~~~*", ]
for x in ABN:
    print(x)
lss = ["Press 1 For Profile",
       "2 For User Credentials",
       "3 For Cash Deposit",
       "4 For Cash Withdrawal",
       "5 For Balance Enquiry",
       "6 For Receipt",
       "7 For Change PIN",
       "8 For Delete Account",
       "9 For Logout"
       ]

while True:
    Fun.Narrator("Press Num Key To Perform Task")
    Key = input("Press Num Key To Perform Task : \n")
    Fun.Narrator("You Select Option "+Key)
    print("*" + "---" * 15 + "*")
    if Key == "1":
        Fun.profile()
        Fun.Narrator("Which is profile")
    elif Key == "2":
        Fun.user_credential()
        Fun.Narrator("Which is User Credentials")
    elif Key == "3":
        Fun.cash_deposit()
        Fun.Narrator("Which is Cash Deposit")
    elif Key == "4":
        Fun.cash_withdrawal()
        Fun.Narrator("Which is Cash WidthDrawl")
    elif Key == "5":
        Fun.balance_enquiry()
        Fun.Narrator("Which is Balance Enquiry")
    elif Key == "6":
        Fun.receipt()
        Fun.Narrator("Which is receipt")
    elif Key == "7":
        Fun.change_pin()
        Fun.Narrator("Which is PIN Change")
        break
    elif Key == "8":
        Fun.delete_account()
    elif Key == "9":
        print("\n Logout")
        Fun.Narrator("Have A nice stay here Good Bye")
        break
    else:
        Fun.Narrator("Which is Invalid Key")
