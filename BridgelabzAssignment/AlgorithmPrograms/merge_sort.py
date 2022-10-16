# MergeSort program in Python

def merge_sort(array):
    try:
        if len(array) > 1:
            div = len(array)//2
            left_sub_arr = array[:div]
            right_sub_arr = array[div:]

            # Sort the two halves
            merge_sort(left_sub_arr)
            merge_sort(right_sub_arr)

            i = j = k = 0
            while i < len(left_sub_arr) and j < len(right_sub_arr):
                if left_sub_arr[i] < right_sub_arr[j]:
                    array[k] = left_sub_arr[i]
                    i += 1
                else:
                    array[k] = right_sub_arr[j]
                    j += 1
                k += 1

            while i < len(left_sub_arr):
                array[k] = left_sub_arr[i]
                i += 1
                k += 1

            while j < len(right_sub_arr):
                array[k] = right_sub_arr[j]
                j += 1
                k += 1
        return array
    except IndexError:
        print("array went out of index")


# Main Method
if __name__ == '__main__':
    try:
        int_array = [16, 25, 12, 10, 9, 2, 100]
        print("given array is : ", int_array)
        merge_sort(int_array)

        print("Sorted array is: ", int_array)
    except Exception:
        print("some error arises")
