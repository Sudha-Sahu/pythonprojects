from phone_book import MyPhoneBook
import json

book = MyPhoneBook(r"C:\Users\HP\PycharmProjects\BridgelabzAssignment\PhoneBookUsingJson\data.json")
while True:
    _choice = input("""Enter you choice : 
                  (a)  Add new contact
                  (b)  View all contact
                  (c)  Modify the contact
                  (d)  Delete the contact
                  (e)  Search by Name/Number
                  (f)  Sort the contact
                  (g)  Quit """)

    if _choice == 'a':
        book.add_contact()
    elif _choice == 'b':
        book.view_all_contacts()
    elif _choice == 'c':
        book.modify_contact()
    elif _choice == 'd':
        book.delete_contact()
    elif _choice == 'e':
        # book.search_contact()
        pass
    elif _choice == 'f':
        # book.sort_contact()
        pass
    elif _choice == 'g':
        break
    else:
        print("You entered something incorrectly, try again(Choose between(a to g)")


result_list = []
for data in book.person_list:
    dict1 = {"Name": data.name, "PhoneNumber": data.phone_number, "Address": data.address}
    result_list.append(dict1)


with open(r"C:\Users\HP\PycharmProjects\BridgelabzAssignment\PhoneBookUsingJson\data.json", 'a+') as out_file:
    json.dump(result_list, out_file)
