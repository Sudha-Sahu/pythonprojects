from datetime import date
import re


if __name__ == "__main__":
    try:
        msg = "Hello <<name>>, We have your full name as <<full name>> in our system. your contact number is " \
              "91-xxxxxxxxxx. \nPlease,let us know in case of any clarification Thank you BridgeLabz 01/01/2016."
        print(msg)

        new_msg = re.sub("<<name>>", input("enter your first name : "), msg)
        new_msg = re.sub("<<full name>>", input("enter your full name : "), new_msg)
        new_msg = re.sub("xxxxxxxxxx", input("enter your mobile number : "), new_msg, 10)
        new_msg = re.sub("01/01/2016", str(date.today()), new_msg)
        print(new_msg)
    except ValueError:
        print("please enter valid inputs")

