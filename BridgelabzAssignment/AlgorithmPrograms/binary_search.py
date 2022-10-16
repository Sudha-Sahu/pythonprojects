# program for searching the number in given array using binary search.

def binary_search_of_number(int_list, low, high, search):
    if low <= high:
        mid = (low + high) // 2
        if int_list[mid] == search:
            return mid
        elif int_list[mid] > search:
            return binary_search_of_number(int_list, low, mid - 1, search)
        else:
            return binary_search_of_number(int_list, mid + 1, high, search)
    else:
        return -1


if __name__ == "__main__":
    try:
        int_array = [12, 56, 89, 89, 90, 95, 99]
        find_num = int(input("enter any number from the list to search: "))

        # Function call
        output = binary_search_of_number(int_array, 0, len(int_array) - 1, find_num)

        if output == -1:
            print("given number is not present in the given list ")
        else:
            print("given number is present in the given list at index : ", output)
    except Exception:
        print("some error arises")


# program for searching the number in given array using binary search.
def binary_search_of_string(string_arr, find_str):
    start = 0
    end = len(string_arr)
    while start <= end:
        m = (start + end) // 2
        res = (find_str == string_arr[m])
        if res == 0:
            return m - 1
        elif res > 0:
            start = m + 1
        else:
            end = m - 1
    return 0


if __name__ == "__main__":
    try:
        fruits = ["apple", "banana", "orange", "papaya", "pear", "mango"]
        search_fruit = input("enter any fruit name to search from the fruit list: ")
        op = binary_search_of_string(fruits, search_fruit)

        if op:
            print("given fruit is present in the fruit list at the index: ", op)
        else:
            print("given fruit is not present in the fruit list")
    except Exception:
        print("some error arises")


# program for searching your number in given range using binary search.
def find_number(low, high):
    mid = (low + high) // 2
    compare = int(input(f"Enter the your choice if your number is : 1.Smaller than\t 2.Equal to\t 3.Greater than {mid} :"))
    if compare == 1:
        find_number(low, mid)
    elif compare == 2:
        print(f"{mid} is your number")
    elif compare == 3:
        find_number(mid, high)
    else:
        print("invalid choice")


if __name__ == "__main__":
    try:
        n = int(input("Enter n for N = 2^n: "))
        print(f"Think of a number between 0 - {2**n}")
        find_number(1, (2**n)-1)
    except ValueError:
        print("please enter valid inputs")
