from DB_Connection import db
from beautifultable import BeautifulTable
from Login import User_Name, PIN_Confirmlg
import datetime as T


y = T.datetime.now()
x = y.strftime("%d/%m/%Y")

f = db.cursor()
f.execute("SELECT * FROM `userinfo` WHERE username='" + User_Name + "' AND pin='" + PIN_Confirmlg + "'")
fd = f.fetchall()
for i in fd:
    ID = i[0]
    Name = i[1]
    F_Name = i[2]
    DOB = i[3]
    User_Name = i[4]
    PIN_Confirm = i[5]
    Total_Amount = i[6]


class Functions:
    def profile(self):
        Table = BeautifulTable()
        Table.columns.header = ["*Fawad ATM Management System*\nUser Profile"]
        Table.rows.append([Name])
        Table.rows.append([F_Name])
        Table.rows.append([DOB])
        Table.rows.append(["FATMS54622JUN20" + str(ID)])
        Table.rows.header = ["  Name ", "  Father Name ", "  Birth Date ", " IBAN  "]
        Table.set_style(BeautifulTable.STYLE_BOX_ROUNDED)
        Table.columns.padding_right[0] = 16
        Table.columns.padding_left[0] = 16
        print(Table)
        self.footer()

    def user_credential(self):
        Table = BeautifulTable()
        Table.columns.header = ["*Fawad ATM Management System*\nUser Credential"]
        Table.rows.append([User_Name])
        Table.rows.append([PIN_Confirm])
        Table.rows.append(["FATMS54622JUN20" + str(ID)])
        Table.rows.header = ["  User Name  ", "  PIN Code ", " IBAN  "]
        Table.set_style(BeautifulTable.STYLE_BOX_ROUNDED)
        Table.columns.padding_right[0] = 17
        Table.columns.padding_left[0] = 16
        print(Table)
        self.footer()

    def cash_deposit(self):
        Current_Amount = 200
        Deposit_Cash = int(input("Enter Your Amount to Deposit in Your Account : "))
        Total_Amount = Current_Amount + Deposit_Cash
        print(f"Congredulation {Deposit_Cash} Ruppess has been Deposited Sucessfully in Your Account on " + y.strftime("%x At %X %p"))

    def cash_withdrawal(self, A, B, C):
        print(A, B, C)

    def balance_enquiry(self):
        Table = BeautifulTable()
        Table.columns.header = ["*Fawad ATM Management System*\nBalance Enquiry"]
        Table.rows.append(["  " * 30])
        Table.set_style(BeautifulTable.STYLE_BOX_ROUNDED)
        Table.columns.padding_right[0] = 16
        Table.columns.padding_left[0] = 16
        table = BeautifulTable()
        table.columns.header = ["Total\nAmount", "Current\nAmount", "Cash\nDeposite", "Cash\nWithdrawl", "Date"]
        table.rows.append([Total_Amount, "2000", "15500", "19000", x])
        table.set_style(BeautifulTable.STYLE_BOX_ROUNDED)
        table.columns.padding_right['Total\nAmount'] = 5
        table.columns.padding_right['Current\nAmount'] = 5
        table.columns.padding_right['Cash\nDeposite'] = 5
        table.columns.padding_right['Cash\nWithdrawl'] = 7
        table.columns.padding_right['Date'] = 7
        print(Table)
        print("|" + "**" * 39 + "|")
        print(table)
        self.footer()

    def receipt(self):
        Table = BeautifulTable()
        Table.columns.header = ["*Fawad ATM Management System*\nAccount Summary/Receipt"]
        Table.rows.append([Name])
        Table.rows.append([F_Name])
        Table.rows.append([DOB])
        Table.rows.append(["FATMS54622JUN20" + str(ID)])
        Table.rows.header = ["  Name ", "  Father Name ", "  Birth Date "," IBAN  "]
        Table.set_style(BeautifulTable.STYLE_BOX_ROUNDED)
        Table.columns.padding_right[0] = 16
        Table.columns.padding_left[0] = 16
        table = BeautifulTable()
        table.columns.header = ["Total\nAmount", "Current\nAmount", "Cash\nDeposite", "Cash\nWithdrawl", "Date"]
        table.rows.append([Total_Amount, "2000", "15500", "19000", x])
        table.set_style(BeautifulTable.STYLE_BOX_ROUNDED)
        table.columns.padding_right['Total\nAmount'] = 5
        table.columns.padding_right['Current\nAmount'] = 5
        table.columns.padding_right['Cash\nDeposite'] = 5
        table.columns.padding_right['Cash\nWithdrawl'] = 7
        table.columns.padding_right['Date'] = 7
        print(Table)
        print("|" + "**" * 39 + "|")
        print(table)
        self.footer()

    def change_pin(self):
        while True:
            old_PIN = input("Enter Your Old PIN Code : ")
            if old_PIN == PIN_Confirm:
                New_PIN = input("\nEnter Your New PIN Code : ")
                while True:
                    New_PIN_Confirm = input("Enter Your New PIN Again : ")
                    if New_PIN == New_PIN_Confirm:
                        f = db.cursor()
                        f.execute("UPDATE `userinfo` SET pin='" + New_PIN_Confirm + "' WHERE username='" + User_Name + "'")
                        db.commit()
                        print("\nYour PIN Changed Successfully ")
                        break
                    else:
                        print("\nPIN New PIN Match Enter Your PIN Again ")

                break
            else:
                print("\nPIN Not Match Enter Your PIN Again")

    def delete_account(self):
        print("\nDo You Really Want to Delete Your Account (Y / N) : ")
        while True:
            Key = input().upper()
            if Key == "Y":
                f = db.cursor()
                f.execute("DELETE FROM `userinfo` WHERE username='" + User_Name + "'")
                db.commit()
                print("\nYour Account has been Deleted Sucessfully ")
                break
            elif Key == "N":
                print("\nYou Have Canceled While Deleting Your Account")
                break
            else:
                print("\nInvalid Key Press (Y or N) : ")

    def footer(self):
        ftr = ["|" + "mm" * 39 + "|",
               "|_________________Copyright@ 2020 Fawad. All Rights Reserved________________v2_|",
               "*~~~~~~~--------------~~First Pro Python Programm Ever~~----------------~~~~~~~*\n\n"]
        for f in ftr:
            print(f)

# f = Functions()
# f.receipt()
