# program to find the prime factors of given input number

import math


def prime_factors(num):
    while num % 2 == 0:
        print(2, )
        num = num // 2

    for i in range(3, int(math.sqrt(num)) + 1, 2):
        while num % i == 0:
            print(i, )
            num = num // i

    if num > 2:
        print(num)


if __name__ == "__main__":
    try:
        number = int(input("enter any number to find its Prime factors : "))
        print("factors of ", number, " are : ")

        # calling function
        prime_factors(number)
    except ValueError:
        print("invalid input from user")
