# print prime number between 1 to 1000
def print_prime():
    """Check and print prime number between 0 to 1000"""
    try:
        prime_list = []
        for number in range(1, 1000):
            count = 0
            for i in range(2, (number // 2 + 1)):
                if number % i == 0:
                    count = count + 1
                    break
            if count == 0 and number != 1:
                prime_list.append(number)
        return prime_list
    except IndexError:
        print("please enter valid inputs")


def check_prime_to_be_palindrome(num):
    """Check the given prime number is palindrome or not"""

    temp = num
    rev = 0
    while num > 0:
        x = num % 10
        rev = rev * 10 + x
        num = num // 10
    if temp == rev:
        return temp


if __name__ == "__main__":
    try:
        print("the prime numbers between 1 and 1000 are: ")
        prime_palin = print_prime()
        print(prime_palin)
        palindrome = []
        print("the prime number which are palindrome also are : ")
        for i in prime_palin:
            if check_prime_to_be_palindrome(i):
                palindrome.append(i)

        print(palindrome)
    except ValueError:
        print("please enter valid inputs")

