# how to declare constant variable in python --> var name should be in capital letters
CONST = 50
print("its a constant variable : ", CONST)


# This is a calculator program using functions
def add(p, q):
    return p + q


def subtract(p, q):
    return p - q


def multiply(p, q):
    return p * q


def divide(p, q):
    return p / q


if __name__ == "__main__":
    print("Please select the operation.")
    print("a. Add")
    print("b. Subtract")
    print("c. Multiply")
    print("d. Divide")

    choice = input("Please enter choice (a/ b/ c/ d): ")

    num_1 = int(input("enter the first number: "))
    num_2 = int(input("enter the second number: "))

    if choice == 'a':
        print(num_1, " + ", num_2, " = ", add(num_1, num_2))
    elif choice == 'b':
        print(num_1, " - ", num_2, " = ", subtract(num_1, num_2))
    elif choice == 'c':
        print(num_1, " * ", num_2, " = ", multiply(num_1, num_2))
    elif choice == 'd':
        print(num_1, " / ", num_2, " = ", divide(num_1, num_2))
    else:
        print("This is an invalid input")
