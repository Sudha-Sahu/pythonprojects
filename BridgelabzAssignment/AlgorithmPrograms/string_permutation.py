# program to generate different permutations of the string


def string_permutation_using_recursion(string, start, end):

    if start == end - 1:
        perm_array.append(string)
    else:
        for x in range(start, end):
            new_str = list(string)
            temp = new_str[start]
            new_str[start] = new_str[x]
            new_str[x] = temp
            # print("new_str : ", new_str)
            string_permutation_using_recursion("".join(new_str), start + 1, end)   # recalling function
    return


if __name__ == "__main__":
    try:
        perm_array = []
        input_str = input("enter any string : ")
        str_len = len(input_str)
        print("All the permutations of the string are : ")
        string_permutation_using_recursion(input_str, 0, str_len)
        print(perm_array)
    except ValueError:
        print("invalid input from user")
