#Program for email validator using regex
import re

def mail_checker(email):
    pattern = "\w+@gmail|outlook|rediffmail.com$"
    obj = re.match(pattern, email)
    if obj:
        return True
    return False

if __name__  == "__main__":
    name = input("Please enter your name here : ")
    print(f"\nWelcome to Command Line email validator program {name}!")
    while True:
        email = input("Please enter your email id (gmail/outlook/rediff only) : ")
        if mail_checker(email):
            print("\nValid email id recognized\n")
            break
        else:
            print("Invalid email!\n")
            response = input("Press Enter to continue or 0 to exit : ")
        if response == "0":
            print("")
            break  

    