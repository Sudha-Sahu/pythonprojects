# Stack implementation in python

class Stack:
    def __init__(self):
        self.stack = []

    # Creating an empty stack
    def check_empty(self):
        return len(self.stack) == 0

    # Adding items into the stack
    def push_element(self, item):
        self.stack.append(item)
        print("pushed item: " + item)

    # Removing an element from the stack1
    def pop_element(self):
        if self.check_empty():
            print("your stack is empty")
        else:
            ele = self.stack.pop()
            print("removed element from stack : ", ele)
            print("the stack after popping : ", self.stack)

    def peek_element(self):
        print("the top element of stack is: ", self.stack[-1])

    def display_stack(self):
        print("the element in stack from bottom to top is: ", self.stack)


if __name__ == "__main__":
    try:
        stack_obj = Stack()
        while True:
            print("Select the operation you want to perform on stack: "
                  "1)add  2)remove 3)display 4)display top element 5)quit")
            choice = int(input())
            if choice == 1:
                element = input("enter the value : ")
                stack_obj.push_element(element)
            elif choice == 2:
                stack_obj.pop_element()
            elif choice == 3:
                stack_obj.display_stack()
            elif choice == 4:
                stack_obj.peek_element()
            elif choice == 5:
                break
            else:
                print("input right operation number!!!")
    except Exception as e:
        print("some error arises")
