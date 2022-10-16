# check whether the given number is palindrome or not
def check_palindrome_num(num):
    try:
        temp = num
        rev = 0
        while num > 0:
            x = num % 10
            rev = rev*10 + x
            num = num//10
        if temp == rev:
            print(temp, "is palindrome!")
        else:
            print(temp, "not a palindrome!")
    except Exception as e:
        print("user hit uninterrupt error")


# check whether the given word is palindrome or not
def check_palindrome_string(word):
        rev_word = reversed(word)

        if list(word) == list(rev_word):
            print(word, "is palindrome!!!!!")
        else:
            print(word, "is not a palindrome!!!!!")


if __name__ == "__main__":
    try:
        number = int(input("Enter a number:"))
        check_palindrome_num(number)

        input_word = input("Enter any word: ")
        check_palindrome_string(input_word)
    except ValueError:
        print("please enter valid inputs")
