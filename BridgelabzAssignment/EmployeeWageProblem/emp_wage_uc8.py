# UC8-storing daily wage

import random

# Constants
WAGE_PER_HR = 20
IS_PART_TIME = 1
IS_FULL_TIME = 2
MAX_WORKING_DAY_PER_MONTH = 20
MAX_WORKING_HOUR_PER_MONTH = 100


# defining a function
def store_daily_wage():
    day_count = 1
    total_working_hr = 0
    store_per_day_wage = []
    while day_count <= MAX_WORKING_DAY_PER_MONTH and total_working_hr < MAX_WORKING_HOUR_PER_MONTH:
        is_present = random.randint(0, 2)
        if is_present == IS_PART_TIME:
            total_working_hr += 4
            daily_hr = 4
        elif is_present == IS_FULL_TIME:
            total_working_hr += 8
            daily_hr = 8
        else:
            total_working_hr += 0
            daily_hr = 0
        daily_wage = daily_hr * WAGE_PER_HR
        store_per_day_wage.append(daily_wage)
        day_count += 1
    print("day wise wage is :", store_per_day_wage)
    total_wage = total_working_hr * WAGE_PER_HR
    return total_wage


if __name__ == "__main__":
    try:
        print("Welcome to employee wage problem")
        # calling a function
        print("Employee total monthly wage is : ", store_daily_wage())
    except Exception:
        print("some thing went wrong please check")
