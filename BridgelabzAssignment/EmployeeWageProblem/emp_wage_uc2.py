# UC2-calculating daily wage

import random

if __name__ == "__main__":
    try:
        wage_per_hr = 20
        working_day_hr = 0
        emp_present = 1

        print("Welcome to employee wage problem")

        attendance = random.randint(0, 1)
        if attendance == emp_present:
            working_day_hr = 8
        else:
            working_day_hr = 0
        daily_wage = working_day_hr * wage_per_hr
        print("Employee daily wage : ", daily_wage)
    except Exception:
        print("some error occur")
