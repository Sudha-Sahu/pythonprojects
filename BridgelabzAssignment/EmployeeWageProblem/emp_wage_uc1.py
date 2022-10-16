# UC1-checking employee attendance

import random

if __name__ == "__main__":
    try:
        print("Welcome to employee wage problem")
        emp_present = 1
        attendance = random.randint(0, 1)
        if attendance == emp_present:
            print("Employee is present")
        else:
            print("Employee is absent")
    except Exception as e:
        print("some thing went wrong please check")

