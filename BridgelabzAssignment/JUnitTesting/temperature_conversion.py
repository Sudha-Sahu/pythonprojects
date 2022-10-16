
def convert_temperature(temp):
    degree = int(temp[:-1])
    i_conv = temp[-1]
    o_conv, convert = 0, ''

    if i_conv.upper() == "C":
        convert = int(round((9 * degree) / 5 + 32))
        o_conv = "Fahrenheit"
    elif i_conv.upper() == "F":
        convert = int(round((degree - 32) * 5 / 9))
        o_conv = "Celsius"
    else:
        print("Input proper convention.")
        quit()
    return o_conv, convert


if __name__ == "__main__":
    try:
        temperature = input("Input the  temperature you like to convert? (e.g., 45F, 102C etc.) : ")
        conv, op_convert = convert_temperature(temperature)
        print(f"The temperature in {conv}, is {op_convert} degrees.")
    except ValueError:
        print("give proper inputs")
