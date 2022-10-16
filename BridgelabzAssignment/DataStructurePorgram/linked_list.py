# linked list in data structure

class Node:
    def __init__(self, data_val=None):
        self.data_val = data_val
        self.next_val = None


class LinkedList:
    def __init__(self):
        self.head_val = None

    # Print the linked list
    def list_print(self):
        print_val = self.head_val
        while print_val is not None:
            print(print_val.data_val)
            print_val = print_val.next_val

    def insert_at_beginning(self, new_data):
        new_node = Node(new_data)

        # Update the new nodes next val to existing node
        new_node.next_val = self.head_val
        self.head_val = new_node

    def insert_at_end(self, new_data):
        new_node = Node(new_data)
        if not self.head_val:
            self.head_val = new_node
            return
        last_node = self.head_val
        while last_node.next_val:
            last_node = last_node.next_val
        print("new node added at the end")
        last_node.next_val = new_node

    def insert_in_between(self, middle_node, new_data):
        if not middle_node:
            print("The mentioned node is absent")
            return

        new_node = Node(new_data)
        new_node.next_val = middle_node.next_val
        middle_node.next_val = new_node
        print("new node inserted at middle of linked list")

        # Function to remove node
    def remove_node(self, remove_key):
        head_val = self.head_val

        if head_val:
            if head_val.data_val == remove_key:
                self.head_val = head_val.next
                head_val = None
                return
        while not head_val:
            if head_val.data_val == remove_key:
                break
            prev = head_val
            head_val = head_val.next_val

        if not head_val:
            return

        prev.next_val = head_val.next
        head_val = None


linked_list = LinkedList()
linked_list.head_val = Node("Mon")
node2 = Node("Tue")
node3 = Node("Wed")

linked_list.head_val.next_val = node2
node2.next_val = node3
linked_list.list_print()

linked_list.insert_at_beginning("Sun")
print("linked list after adding new node at beginning.......")
linked_list.list_print()
print("linked list after adding new node at end.......")
linked_list.insert_at_end("thu")
linked_list.list_print()
print("linked list after adding new node at middle.......")
linked_list.insert_in_between(linked_list.head_val, "I am in between the list")
linked_list.list_print()
linked_list.remove_node("wed")
linked_list.list_print()
