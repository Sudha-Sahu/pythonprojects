# program to calculate the square root of any positive number

def sqrt_using_newton_method(number):
    epsilon = 1e-15
    t = number

    while abs(t - number/t) > epsilon*t:
        t = (number/t + t) / 2
    print("the square root of ", number," is : ", t)


num = int(input("enter any non negative number to find its square root : "))
sqrt_using_newton_method(num)
