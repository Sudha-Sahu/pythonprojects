# UC4-solving using switch case statement and calculating wage

import random

# Constants
WAGE_PER_HR = 20
PART_TIME_HR = 4
FULL_DAY_HR = 8


def calc_emp_wage():

    # calculating the daily employee wage
    wage_full_day = WAGE_PER_HR * FULL_DAY_HR
    print('Wage per day in full time hr is : {}'.format(wage_full_day))

    # calculating the part-time employee wage
    part_time_emp_wage = WAGE_PER_HR * PART_TIME_HR
    print('Part Time Wage per day is : {}'.format(part_time_emp_wage))
    wage = {
        0: {'is_present': 'absent', 'wage': 0, 'worked_hr': 0},
        1: {'is_present': 'present-full-day', 'wage': wage_full_day, 'worked_hr': FULL_DAY_HR},
        2: {'is_present': 'part-time', 'wage': part_time_emp_wage, 'worked_hr': PART_TIME_HR}
    }
    return wage


if __name__ == "__main__":
    try:
        print("Welcome to employee wage problem")
        is_present = random.randint(0, 2)
        emp_wage = calc_emp_wage()
        print("Employee daily wage : ", emp_wage.get(is_present))
    except Exception as e:
        print("some thing went wrong please check")
