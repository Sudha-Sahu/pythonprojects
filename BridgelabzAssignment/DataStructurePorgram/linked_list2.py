class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beg(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = Node(data, None)
        return

    def insert_values(self, data_list):
        for i in data_list:
            self.insert_at_end(i)
        return

    def display(self):
        if self.head is None:
            print("Linked List is Empty")
            return
        temp = self.head
        while temp:
            print(f"{temp.data}-->", end=' ')
            temp = temp.next
        print()

    def is_present(self, data):
        temp = self.head
        while temp:
            if temp.data == data:
                return True
            temp = temp.next
        return False

    def remove(self, data):
        temp = self.head
        if self.is_present(data):
            while temp:
                if temp.next.data == data:
                    temp.next = temp.next.next
                    return
                temp = temp.next
        else:
            print(f"{data} is not present")

    def remove_last(self):
        if self.head:
            if self.head.next is None:
                self.head = None
            else:
                temp = self.head
                while temp.next.next:
                    temp = temp.next
                temp.next = None

    def get_last(self):
        if self.head:
            if self.head.next is None:
                return self.head.data
            else:
                temp = self.head
                while temp.next:
                    temp = temp.next
                return temp.data

    def add_num_to_sorted(self, number):
        temp = self.head
        if temp.data >= number:
            self.insert_at_beg(number)
            return
        while temp.next:
            if temp.next.data >= number:
                node = Node(number, temp.next)
                temp.next = node
                return
            temp = temp.next
        if temp.next is None:
            self.insert_at_end(number)

    def to_string(self):
        temp = self.head
        string_ = " "
        if isinstance(temp.data, int):
            while temp:
                string_ += f"{temp.data} "
                temp = temp.next
            return string_
        else:
            while temp:
                string_ += temp.data + " "
                temp = temp.next
            return string_

    def length(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count