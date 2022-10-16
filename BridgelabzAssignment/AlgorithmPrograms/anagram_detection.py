# program to check whether two strings are anagrams of each other
def check_anagram(str1, str2):
    str_len1 = len(str1)
    str_len2 = len(str2)
    if str_len1 != str_len2:
        return 0
    # Sort both strings using builtin sorted function
    str1 = sorted(str1)
    str2 = sorted(str2)
    print(str1, str2)
    # Compare sorted strings
    for i in range(0, str_len1):
        if str1[i] != str2[i]:
            return 0
    return 1


if __name__ == "__main__":
    try:
        s1 = input("enter the first word:")
        s2 = input("enter the second word:")
        op = check_anagram(s1, s2)

        if op:
            print("The two strings are anagram of each other")
        else:
            print("The two strings are not anagram of each other")
    except ValueError:
        print("invalid input from user")
