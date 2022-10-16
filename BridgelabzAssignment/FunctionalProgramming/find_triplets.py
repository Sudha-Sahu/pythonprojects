# A Python program to find Sum of three Integer adds to ZERO

def find_triplets(arr, n):
    found = False
    count = 0
    for i in range(0, n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if arr[i] + arr[j] + arr[k] == 0:
                    count += 1
                    print(arr[i], arr[j], arr[k])
                    found = True
    print(f"the number of distinct triplets are : {count} ")
    if not found:
        print("triplets not exist ")


if __name__ == "__main__":
    try:
        size = int(input("enter number of integer : "))
        int_arr = []
        for i in range(size):
            int_arr.append(int(input(f"enter value{i + 1} : ")))

        find_triplets(int_arr, size)
    except Exception:
        print("enter valid inputs")
