# Coupon Number program

import random


def coupon_num(input_random, num):
    distinct_arr = []
    print("The distinct coupon number are : ")
    for i in range(num):
        j = 0
        for j in range(i):
            if input_random[i] == input_random[j]:
                break
        if i == j:
            distinct_arr.append(input_random[i])
            print(input_random[i])

    return distinct_arr


if __name__ == "__main__":
    try:
        number = int(input("How many random number you want to generate : "))
        input_ran = []
        for x in range(number):
            input_ran.append(random.randint(1, 100))
        print("The random coupon number are : ", input_ran)
        print(coupon_num(input_ran, number))
    except Exception:
        print("enter valid inputs")

