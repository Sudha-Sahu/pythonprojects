from linked_list2 import LinkedList


if __name__ == "__main__":
    link = LinkedList()
    with open("textfile.txt", 'r+') as file:
        data_file = file.read()
        file.truncate(0)
    list_file = data_file.split(" ")
    link.insert_values(list_file)
    data = "mini"
    present = link.is_present(data)
    if present:
        link.remove(data)
    else:
        link.insert_at_end(data)
    string_ = link.to_string()
    with open("textfile.txt", 'w') as file1:
        file1 = open("textfile.txt", 'w')
        file1.write(string_)
