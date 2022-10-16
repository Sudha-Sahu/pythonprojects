# Program to convert decimal number to binary  and vice versa

def decimal_to_binary(dec_num):

    if dec_num >= 1:
        decimal_to_binary(dec_num // 2)
    print(dec_num % 2, end='')


def binary_to_decimal(bin_num):
    b_num = bin_num
    decimal, i, n = 0, 0, 0
    while bin_num != 0:
        dec = bin_num % 10
        decimal = decimal + dec * (2**i)
        bin_num = bin_num // 10
        i = i+1
    print("the decimal conversion of ", b_num, "is : ", decimal)


if __name__ == "__main__":
    num1 = int(input("enter any decimal number : "))
    decimal_to_binary(num1)

    num2 = int(input("\nenter any binary number : "))
    binary_to_decimal(num2)
