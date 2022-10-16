# program to print the day name of given input date

class DayOfWeek:
    check = True
    get_day_name = ""
    while check:
        check = False
        m = int(input("enter the month: "))
        if m < 1 or m > 12:
            print("Months should be between 1 and 12")
            continue

        d = int(input("enter the day: "))
        if d < 1 or d > 31:
            print("Days should be between 1 and 31")
            continue

        y = int(input("enter the year: "))
        if y < -10000 or y > 10000:
            print("Years should be between -10000 and 10000")
            continue

        y0 = y - (14 - m) / 12
        x = y0 + y0/4 - y0/100 + y0/400
        m0 = m + 12 * ((14 - m) / 12) - 2
        d0 = (d + x + 31 * m0 / 12) % 7
        day = 0 <= d0 <= 6

        if day:
            get_day_name = "Sunday"
        elif day:
            get_day_name = "Monday"
        elif day:
            get_day_name = "Tuesday"
        elif day:
            get_day_name = "Wednesday"
        elif day:
            get_day_name = "Thursday"
        elif day:
            get_day_name = "Friday"
        elif day:
            get_day_name = "Saturday"

        print("The day of the week is: ", get_day_name)


