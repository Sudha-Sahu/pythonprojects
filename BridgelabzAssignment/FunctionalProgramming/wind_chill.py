# calculating the effective temperature
def calc_temperature(temperature, wind_speed):
    if temperature > 50 and (wind_speed > 120 or wind_speed < 3):
        return "invalid inputs"
    else:
        effective_temperature = 35.74 + 0.6215*temperature + (0.4275*temperature - 35.75) * wind_speed**0.16
        return f"the effective temperature of national weather services is : {effective_temperature}"


if __name__ == "__main__":
    try:
        temp = int(input("Enter temperature in Fahrenheit :"))
        speed = int(input("Enter wind speed in miles per hour :"))
        print(calc_temperature(temp, speed))
    except ValueError:
        print("enter valid inputs")

