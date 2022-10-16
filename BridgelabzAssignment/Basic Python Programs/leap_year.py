# Checking given year is leap year or not

def leap_year(year):
    """This function find the given year is leap year or not.
    It has one parameter which is a year."""

    if (year > 999) and (year < 10000):
        if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
            return f"{year}is a Leap year"
        else:
            return f"{year} is not a Leap Year"
    else:
        return "invalid inputs"


if __name__ == "__main__":
    try:
        yr = int(input("Enter any year to check if it is leap year or not : "))
        print(leap_year(yr))
    except ValueError:
        print("invalid input from user")
