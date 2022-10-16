from person import Person
import json


class MyPhoneBook:
    def __init__(self, filepath):
        with open(filepath) as file:
            self.json_data = json.load(file)
        self.person_list = []
        for data in self.json_data:
            self.person_list.append(Person(**data))

    def add_contact(self):
        while True:
            is_present, _name = self.validate()
            if is_present:
                print(f"{_name.name} Already Exist!!")
                break
            phone_number = int(input("Enter Phone Number:"))
            contact_address = input("enter contact address : ")
            person = Person(_name, phone_number, contact_address)
            self.person_list.append(person)
            print("Contact Added!")

    def view_all_contacts(self):
        print('\n', "Listing Contacts...")
        for data in self.person_list:
            print(f"{data.name} \t {data.phone_number} \t {data.address}")

    def modify_contact(self):
        while True:
            is_present, person = self.validate()
            if is_present:
                option = int(input("What do you want to modify:\n1.Name\n2.Phone Number\n"))
                if option == 1:
                    new_name = input("Enter new Name:")
                    phone_num = person.phone_number
                    self.person_list.remove(person)
                    temp_person = Person(new_name, phone_num, )
                    self.person_list.append(temp_person)
                    self.display_one(new_name)
                    return
                if option == 2:
                    new_phone = int(input("Enter New Phone Number:"))
                    nam = person.name
                    self.person_list.remove(person)
                    temp_person = Person(nam, new_phone, )
                    self.person_list.append(temp_person)
                    self.display_one(nam)
                    return
            print(f"{person} is not Present")

    def delete_contact(self):
        while True:
            is_present, person = self.validate()
            if is_present:
                self.person_list.remove(person)
                self.view_all_contacts()
                return
            print(f"{person} is not present")

    def validate(self):
        is_present = False
        name = input("Enter Name:")
        for data in self.person_list:
            if data.name == name:
                is_present = True
                person = data
                return is_present, person
        return is_present, name

    def display_one(self, name):
        for data in self.person_list:
            if data.name == name:
                print(f"{data.name} \t {data.phone_number}")
                return
        print(f"{name} is not present")


'''
    def search_contact(self, search_by):
        s_no = search_by
        s_no_value = 1
        fetch_contact = 'contact fetched by s_no which is equal to 1'
        return fetch_contact

    def sort_contact(self, sort_key):
        value_of_sort_key = sort_key
        all_contacts = self.view_all_contacts(value_of_sort_key)
        return all_contacts
'''
