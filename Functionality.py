from DB_Connection import db
import smtplib
import pyttsx3
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from beautifultable import BeautifulTable
from Narrator import Narrator
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
    Email = i[4]
    User_Name = i[5]
    PIN_Confirm = i[6]
    Previous_Amount = i[7]
    Deposit_Amount = i[8]
    Withdrawal_Amount = i[9]
    Current_Amount = i[10]


class Functions:

    def Narrator(self, command):
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        rate = engine.getProperty('rate')
        engine.setProperty('voice', voices[0].id)
        engine.setProperty('rate', 175)
        engine.say(command)
        engine.runAndWait()

    def profile(self):
        Table = BeautifulTable()
        Table.columns.header = ["*Fawad ATM Management System*\nUser Profile"]
        Table.rows.append([Name])
        Table.rows.append([F_Name])
        Table.rows.append([DOB])
        Table.rows.append(["FATMMS54622JUN20" + str(ID)])
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
        Table.rows.append(["FATMMS54622JUN20" + str(ID)])
        Table.rows.header = ["  User Name  ", "  PIN Code ", " IBAN  "]
        Table.set_style(BeautifulTable.STYLE_BOX_ROUNDED)
        Table.columns.padding_right[0] = 17
        Table.columns.padding_left[0] = 16
        print(Table)
        self.footer()

    def cash_deposit(self):
        Narrator("Enter Your Money Amount to Deposit in Your Account : ")
        Deposit_Cash = int(input())
        Current_Amount = Deposit_Cash + Previous_Amount
        Narrator(
            f"\nPleasure To Inform You That {Deposit_Cash} Rupees has been Deposited Successfully in Your Account on " + x + " And Your Record will be Updated in 24 Hrs")
        f = db.cursor()
        f.execute(
            "UPDATE `userinfo` SET current_amount='" + str(Current_Amount) + "' WHERE username='" + User_Name + "'")
        f.execute("UPDATE `userinfo` SET deposit_amount='" + str(Deposit_Cash) + "' WHERE username='" + User_Name + "'")
        db.commit()

    def cash_withdrawal(self):
        if Current_Amount < 100:
            Narrator("Sorry You Cannot Withdrawal Money Because You Don't have Enough Money In Your Account ")
        else:
            Narrator("\nEnter Your Money Amount You Want To Withdrawal From Your Account You Have " + str(
                Current_Amount) + " Rupees In Your Account ")
            Withdrawal_Cash = int(input())
            Current_Amount1 = Current_Amount - Withdrawal_Cash
            Narrator(
                f"You Have Successfully Withdrawal Amount Of {Withdrawal_Cash} Rupees From Your Account on " + x + " And Your Record will be Updated in 24 Hrs")
            f = db.cursor()
            f.execute(
                "UPDATE `userinfo` SET current_amount='" + str(
                    Current_Amount1) + "' WHERE username='" + User_Name + "'")
            f.execute("UPDATE `userinfo` SET withdrawal_amount ='" + str(
                Withdrawal_Cash) + "' WHERE username='" + User_Name + "'")
            db.commit()

    def balance_enquiry(self):
        Table = BeautifulTable()
        Table.columns.header = ["*Fawad ATM Management System*\nBalance Enquiry"]
        Table.rows.append(["  " * 30])
        Table.set_style(BeautifulTable.STYLE_BOX_ROUNDED)
        Table.columns.padding_right[0] = 16
        Table.columns.padding_left[0] = 16
        table = BeautifulTable()
        table.columns.header = ["Previous\nAmount", "Cash\nDeposite", "Cash\nWithdrawl", "Current\nAmount", "Date"]
        table.rows.append([Previous_Amount, Deposit_Amount, Withdrawal_Amount, Current_Amount, x])
        table.set_style(BeautifulTable.STYLE_BOX_ROUNDED)
        table.columns.padding_right['Previous\nAmount'] = 5
        table.columns.padding_right['Cash\nDeposite'] = 5
        table.columns.padding_right['Cash\nWithdrawl'] = 5
        table.columns.padding_right['Current\nAmount'] = 5
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
        Table.rows.append(["FATMMS54622JUN20" + str(ID)])
        Table.rows.header = ["  Name ", "  Father Name ", "  Birth Date ", " IBAN  "]
        Table.set_style(BeautifulTable.STYLE_BOX_ROUNDED)
        Table.columns.padding_right[0] = 16
        Table.columns.padding_left[0] = 16
        table = BeautifulTable()
        table.columns.header = ["Previous\nAmount", "Cash\nDeposite", "Cash\nWithdrawl", "Current\nAmount", "Date"]
        table.rows.append([Previous_Amount, Deposit_Amount, Withdrawal_Amount, Current_Amount, x])
        table.set_style(BeautifulTable.STYLE_BOX_ROUNDED)
        table.columns.padding_right['Previous\nAmount'] = 5
        table.columns.padding_right['Cash\nDeposite'] = 5
        table.columns.padding_right['Cash\nWithdrawl'] = 5
        table.columns.padding_right['Current\nAmount'] = 5
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
                        f.execute(
                            "UPDATE `userinfo` SET pin='" + New_PIN_Confirm + "' WHERE username='" + User_Name + "'")
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

    def send_email(self):
        message = f"""<html> <body> <h1 style="text-align: center;color: red">Fawad ATM Management 
        System</h1><br><br> <h4 style="text-align: center;">Hey! Dear Most Strongly Welcome To FATMMS<br> Your 
        Account has been Created Successfully <br> Your Account Summary is </h4> <table style="width: 100%;"> <tr 
        style="background-color: green;color:white"> <th style="border: 2px solid #dddddd;text-align: center;padding: 
        8px;">Name</th> <th style="border: 2px solid #dddddd;text-align: center;padding: 8px;">F.Name</th> <th 
        style="border: 2px solid #dddddd;text-align: center;padding: 8px;">User Name</th> <th style="border: 2px 
        solid #dddddd;text-align: center;padding: 8px;">PIN</th> <th style="border: 2px solid #dddddd;text-align: 
        center;padding: 8px;">Amount</th> </tr>
        <tr> 
            <td style="border: 2px solid #dddddd;text-align: center;padding: 8px;"><b>{i[1]}</b></td> 
            <td style="border: 2px solid #dddddd;text-align: center;padding: 8px;"><b>{i[2]}</b></td>
            <td style="border: 2px solid #dddddd;text-align: center;padding: 8px;"><b>{i[4]}</b></td>
            <td style="border: 2px solid #dddddd;text-align: center;padding: 8px;"><b>{i[5]}</b></td>
            <td style="border: 2px solid #dddddd;text-align: center;padding: 8px;"><b>{i[6]}</b></td>
          </tr>
        </table>
        <p style="position:fixed;bottom:0;width: 100%;background-color:black;color:yellow;text-align:center">Copyright@ 2020 Fawad. All Rights Reserved</P>
        </body>
        </html>"""
        msg = MIMEMultipart()
        msg["From"] = "Fawad ATM Managment System"
        msg["To"] = i[1]
        msg["Subject"] = "Most Strongly Welcome To FATMS"
        msg["Bcc"] = i[7]
        msg.attach(MIMEText(message, 'html'))
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login('email@gmail.com', 'pass')
        server.sendmail("email@gmail.com", i[7], msg.as_string())
        server.quit()
        print("\nPlease Check Your Email Inbox For Account Details")
