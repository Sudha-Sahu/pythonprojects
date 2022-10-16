# UC7-refactoring the employee wage using functions

import random

# Constants
WAGE_PER_HR = 20
IS_PART_TIME = 1
IS_FULL_TIME = 2
MAX_WORKING_DAY_PER_MONTH = 20
MAX_WORKING_HOUR_PER_MONTH = 100


# defining a function
def get_total_worked_hrs():
    day_count = 1
    total_working_hr = 0
    while day_count <= MAX_WORKING_DAY_PER_MONTH and total_working_hr < MAX_WORKING_HOUR_PER_MONTH:
        is_present = random.randint(0, 2)
        if is_present == IS_PART_TIME:
            total_working_hr += 4
        elif is_present == IS_FULL_TIME:
            total_working_hr += 8
        else:
            total_working_hr += 0
        print("total working hrs till day ", day_count, " is : ", total_working_hr)
        day_count += 1

    total_wage = total_working_hr * WAGE_PER_HR
    return total_wage


if __name__ == "__main__":
    try:
        print("Welcome to employee wage problem")
        # calling a function
        print("Employee total monthly wage is : ", get_total_worked_hrs())
    except Exception:
        print("some thing went wrong please check")
