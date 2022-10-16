# sort the string using Insertion sort


def insertion_sort(string_array):
    try:
        for x in range(0, len(string_array)):
            key = string_array[x]
            j = x - 1
            while j >= 0 and key < string_array[j]:
                string_array[j + 1] = string_array[j]
                j = j - 1
            string_array[j + 1] = key
    except KeyError:
        print("key error arises ")


if __name__ == "__main__":
    try:
        num = int(input("enter the number : "))
        str_arr = []
        print("enter string to sort it : ")
        for i in range(num):
            str_arr.append(input())
        insertion_sort(str_arr)
        print('Sorted Array of string are :')
        print(str_arr)
    except ValueError:
        print("please enter valid inputs")
