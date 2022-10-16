# program to print 2D array in python using list

def print_2d_array(arr, row, col):
    print("Enter the values in array :")
    # nested for loop for entering value in 2d array
    for x_row in range(row):
        _1d_array = []
        for y_row in range(col):
            _1d_array.append(int(input()))
        arr.append(_1d_array)
    return arr


if __name__ == "__main__":
    try:
        # taking number of rows and column from user
        r = int(input("Enter the number of rows:"))
        c = int(input("Enter the number of columns:"))
        # Initialize 2D Array
        array = []
        # calling the function
        array = print_2d_array(array, r, c)
        # nested For loop for printing the 2d array
        print("The matrix representation of 2D array is : ")
        for i in range(r):
            for j in range(c):
                print(array[i][j], end=" ")
            print()
    except Exception:
        print("invalid input from user")
