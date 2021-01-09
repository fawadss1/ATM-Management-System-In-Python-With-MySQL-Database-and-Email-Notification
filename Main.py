from Narrator import Narrator


print("\t" * 14 + "*" + "--" * 27 + "*")
Narrator("\t" * 14 + "| Most Strongly Welcome to Fawad ATM Management System |")
print("\t" * 14 + "*" + "--" * 27 + "*")
try:
    while True:
        print("*" + "---" * 15 + "*")
        Narrator("For Sign Up Press(1) For Login Press (2)")
        varify = input()
        print("*" + "---" * 15 + "*")
        if varify == "1":
            import Sign_Up
            break
        elif varify == "2":
            import Login
            break
        else:
            Narrator("Invalid Key Please Try Again")
    import Welcome
except:
    pass

# External Packages Used in this Project
# beautifultable
# mysql-connector-python
# pyttsx3
