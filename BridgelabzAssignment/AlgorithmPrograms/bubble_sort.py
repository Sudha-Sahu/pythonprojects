# sort integer using bubble sort


def bubble_sort(arr):
    try:
        n = len(arr)
        for k in range(n - 1):
            flag = 0
            for j in range(n - 1):
                if arr[j] > arr[j + 1]:
                    temp = arr[j]
                    arr[j] = arr[j + 1]
                    arr[j + 1] = temp
                    flag = 1

            if flag == 0:
                break
        return arr
    except IndexError:
        print("array went out of index")


if __name__ == "__main__":
    try:
        num = int(input("enter the number : "))
        int_arr = []
        print("enter numbers to sort it : ")
        for i in range(num):
            int_arr.append(input())

        op = bubble_sort(int_arr)
        print(op)
    except ValueError:
        print("please enter valid inputs")
