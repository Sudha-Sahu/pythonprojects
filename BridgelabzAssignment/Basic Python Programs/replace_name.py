# Replace string template with Any Name

def replace_name(new_name):
    try:
        if len(new_name) >= 3:
            return new_name

    except ValueError:
        return "invalid input from user"


if __name__ == "__main__":
    print('Hello <<name>>, How are you?')
    name = input("Enter your name : ")
    name = replace_name(name)
    print(f'Hello {name}, How are you?')
