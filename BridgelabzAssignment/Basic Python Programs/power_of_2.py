# Calculating power of 2

def calc_power(num):
    i = 1
    power = 1
    while i <= num:
        power = power * 2
        i = i+1

    return power


if __name__ == "__main__":
    try:
        int_num = int(input("enter any number to calculate power of two : "))
        print(f"power of two upto {int_num} is : ", calc_power(int_num))
    except ValueError:
        print("invalid input from user")
