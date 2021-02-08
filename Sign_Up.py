welcome_message = lambda: print("Congratulations! Registration has been Completed Successfully")
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from Narrator import Narrator

try:
    from DB_Connection import db

    Narrator("Please Enter Your Good Name : ")
    Name = input().capitalize()
    print("*" + "---" * 15 + "*")
    Narrator("Please Enter Your Father Name : ")
    F_Name = input().capitalize()
    print("*" + "---" * 15 + "*")
    Narrator("Please Enter Your Date of Birth")
    try:
        Narrator("Enter Day : ")
        DD = int(input())
        Narrator("Enter Month in Figure : ")
        MM = int(input())
        Narrator("Enter Year : ")
        YYY = int(input())
        print("*" + "---" * 15 + "*")
        if 1 <= DD <= 31 and 1 <= MM <= 12 and 1947 <= YYY <= 2002:
            DOB = "0" + str(DD) + "/0" + str(MM) + "/" + str(YYY)
            Narrator("Enter Your Money Amount Between (100-100000) : ")
            Previous_Amount = int(input())
            print("*" + "---" * 15 + "*")
            while Previous_Amount < 100 or Previous_Amount > 100000:
                Narrator("Invalid Range Enter Your Money Amount Again (100-100000) : ")
                Previous_Amount = int(input())
            Narrator("Please Enter Your Email Address : ")
            Email = input()
            print("*" + "---" * 15 + "*")
            Narrator("Please Enter Your User Name : ")
            User_Name = input().lower()
            print("*" + "---" * 15 + "*")
            while True:
                Narrator("Please Enter Your 4 Digits Pin : ")
                PIN = input().lower()
                if len(PIN) == 4:
                    break
                else:
                    Narrator("Invalid Your PIN Code Must Be 4 Digits Only")
                print("*" + "---" * 15 + "*")
            while True:
                Narrator("Enter Your 4 Digits PIN Again : ")
                PIN_Confirm = input()
                if PIN_Confirm == PIN:
                    print("*" + "---" * 15 + "*")
                    break
                else:
                    Narrator("Sorry Your PIN Does not Match Try Again")
                    print("*" + "---" * 15 + "*")


            def send_email():
                message = f"""<html> <body> <h1 style="text-align: center;color: red">Fawad ATM Management 
                 System</h1><br><br> <h4 style="text-align: center;">Hey! Dear Most Strongly Welcome To FATMMS<br> Your 
                 Account has been Created Successfully <br> Your Account Summary is </h4> <table style="width: 100%;"> <tr 
                 style="background-color: green;color:white"> <th style="border: 2px solid #dddddd;text-align: center;padding: 
                 8px;">Name</th> <th style="border: 2px solid #dddddd;text-align: center;padding: 8px;">F.Name</th> <th 
                 style="border: 2px solid #dddddd;text-align: center;padding: 8px;">User Name</th> <th style="border: 2px 
                 solid #dddddd;text-align: center;padding: 8px;">PIN</th> <th style="border: 2px solid #dddddd;text-align: 
                 center;padding: 8px;">Amount</th> </tr>
                 <tr> 
                     <td style="border: 2px solid #dddddd;text-align: center;padding: 8px;"><b>{Name}</b></td> 
                     <td style="border: 2px solid #dddddd;text-align: center;padding: 8px;"><b>{F_Name}</b></td>
                     <td style="border: 2px solid #dddddd;text-align: center;padding: 8px;"><b>{User_Name}</b></td>
                     <td style="border: 2px solid #dddddd;text-align: center;padding: 8px;"><b>{PIN_Confirm}</b></td>
                     <td style="border: 2px solid #dddddd;text-align: center;padding: 8px;"><b>{Previous_Amount}</b></td>
                   </tr>
                 </table>
                 <p style="position:fixed;bottom:0;width: 100%;background-color:black;color:yellow;text-align:center">Copyright@ 2020 Fawad. All Rights Reserved</P>
                 </body>
                 </html>"""
                msg = MIMEMultipart()
                msg["From"] = "Fawad ATM Management System"
                msg["To"] = Name
                msg["Subject"] = "Most Strongly Welcome To FATMS"
                msg["Bcc"] = Email
                msg.attach(MIMEText(message, 'html'))
                server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
                server.login('email@gmail.com', 'pass')
                server.sendmail("email@gmail.com", Email, msg.as_string())
                server.quit()
                print("\n" + "|" + "**" * 38 + "|")
                Narrator("|\t\t\t\tPlease Check Your Email Inbox For Account Details" + " " * 12 + "|")
                print("|" + "**" * 38 + "|")


            f = db.cursor()
            f.execute("CREATE TABLE IF NOT EXISTS `userinfo` (id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(255),father_name "
                    "VARCHAR(255),dob VARCHAR(255),email VARCHAR(255),username VARCHAR(255),pin VARCHAR(11),previous_amount INT,deposit_amount INT,withdrawal_amount INT,current_amount INT)")
            f.execute("SELECT * FROM `userinfo` WHERE username= '" + User_Name + "'")
            f.fetchall()
            if f.rowcount > 0:
                Narrator("\nThis User Name is Already Registered Please Login To Your Account")
            else:
                f.execute(
                    "INSERT INTO `userinfo` (name,father_name,dob,email,username,pin,previous_amount) VALUES ('" + Name + "','" + F_Name + "','" + DOB + "','" + Email + "','" + User_Name + "','" + PIN_Confirm + "','" + str(
                        Previous_Amount) + "')")
                db.commit()
                # welcome_message()
                Narrator("Congratulations!Registration has been Completed Successfully")
                try:
                    send_email()
                except:
                    print("\n" + "|" + "**" * 38 + "|")
                    Narrator("|\t\t\t\tSorry! Email Cannot Be Send Due to Server Error" + " " * 14 + "|")
                    print("|" + "**" * 38 + "|")
                import Login
        else:
            Narrator("Invalid Values Or You Are Under Age Thank You")

    except ValueError:
        print("|" + "**" * 54 + "|")
        Narrator(
            "|\t\t\t\t\tInvalid Values System is not Responding Please Press (Shift+F10) To Refresh" + "  " * 7 + "|")
        print("|" + "**" * 54 + "|")
except:
    print("\n" + "|" + "**" * 38 + "|")
    Narrator("|\t\t\t\tYour DataBase Server is Down! Please Try Again" + " " * 15 + "|")
    print("|" + "**" * 38 + "|")
