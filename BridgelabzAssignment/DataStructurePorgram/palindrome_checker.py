from collections import deque


def reverse_by_deque(string_):
    container = deque()
    for i in string_:
        container.append(i)

    op_string = ""
    for i in range(len(string_)):
        op_string += container[-1]
        container.pop()
    return op_string


if __name__ == "__main__":
    try:
        input_string = input("Enter string to be checked:")
        rev_string = reverse_by_deque(input_string)
        if rev_string == input_string:
            print(rev_string, "is Palindrome")
        else:
            print(rev_string, "is not Palindrome")
    except ValueError:
        print("give valid inputs")
