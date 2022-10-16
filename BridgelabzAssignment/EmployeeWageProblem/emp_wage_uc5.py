# UC5-calculating wages for a month

import random

# Constants
WAGE_PER_HR = 20
IS_PART_TIME = 1
IS_FULL_TIME = 2
WORKING_DAY_PER_MONTH = 20


def calc_emp_wage():
    day_count = 1
    total_wage = 0

    while day_count <= WORKING_DAY_PER_MONTH:
        is_present = random.randint(0, 2)
        if is_present == IS_PART_TIME:
            working_day_hr = 4
        elif is_present == IS_FULL_TIME:
            working_day_hr = 8
        else:
            working_day_hr = 0
        wage_per_day = working_day_hr * WAGE_PER_HR
        print("Employee wage in day ", day_count, " is : ", wage_per_day)
        total_wage += wage_per_day
        day_count += 1

    return total_wage


if __name__ == "__main__":
    try:
        print("Welcome to employee wage problem")
        print(f"Employee total monthly wage is : {calc_emp_wage()}")

    except Exception:
        print("some thing went wrong please check")
