from linked_list2 import LinkedList


def string_to_list(num_str):
    _list = num_str.split()
    list_ = list(map(int, _list))
    return list_


if __name__ == "__main__":
    link = LinkedList()
    with open("num_file.txt", 'r+') as file:
        number_string = file.read()
        file.truncate(0)

    number_list = string_to_list(number_string)
    number_list.sort()

    link.insert_values(number_list)
    # link.display()

    user_number = int(input("Enter any number : "))

    present = link.is_present(user_number)
    if present:
        link.remove(user_number)
    else:
        link.add_num_to_sorted(user_number)
    # link.display()

    string_ = link.to_string()
    with open("num_file.txt", 'w') as file:
        file.write(string_)

