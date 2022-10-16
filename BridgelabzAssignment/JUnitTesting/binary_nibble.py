from JUnitTesting import binary_decimal_conv as bd


# Function for swap nibble
def swap_nibbles(num):
    return num[4:9] + num[0:4]


if __name__ == "__main__":
    try:
        number = int(input("Enter a decimal number to swap value: "))
        binary_number = bd.decimal_to_binary(number)
        swapped_number = swap_nibbles(binary_number)
        print("Resultant number after swapping nibbles is {}".format(swapped_number))
    except Exception as e:
        print("{} is raised.".format(str(e)))

