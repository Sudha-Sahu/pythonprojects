# UC3-adding part time employee and calculating wage

import random

WAGE_PER_HR = 20
IS_PART_TIME = 1
IS_FULL_TIME = 2


def calc_emp_wage(is_present):
    if is_present == IS_PART_TIME:
        working_day_hr = 4
    elif is_present == IS_FULL_TIME:
        working_day_hr = 8
    else:
        working_day_hr = 0

    daily_wage = working_day_hr * WAGE_PER_HR
    return daily_wage


if __name__ == "__main__":
    try:
        working_hr = 0
        print("Welcome to employee wage problem")
        present = random.randint(0, 2)
        print("Employee daily wage : ", calc_emp_wage(present))

    except Exception:
        print("some error occured")
