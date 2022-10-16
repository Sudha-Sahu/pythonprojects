
class Queue:
    def __init__(self):
        self.queue = []

    # Add an element
    def enqueue(self):
        element = input("enter the value : ")
        self.queue.append(element)
        print(element, "is added to queue!!!")

    # Remove an element
    def dequeue(self):
        if len(self.queue) < 1:
            print("queue is empty")
        else:
            del_element = self.queue.pop(0)
            print("deleted the element : ", del_element)

    # Display  the queue
    def display_queue(self):
        print(self.queue)

    def size(self):
        return len(self.queue)


q_obj = Queue()

while True:
    print("Select the operation you want to perform on queue: 1)add  2)remove 3)show 4)size of queue 5)quit")
    choice = int(input())
    if choice == 1:
        q_obj.enqueue()
    elif choice == 2:
        q_obj.dequeue()
    elif choice == 3:
        q_obj.display_queue()
    elif choice == 4:
        q_obj.size()
    elif choice == 5:
        break
    else:
        print("input right operation number!!!")


# deque in python
"""
A double-ended queue, or deque, has the feature of adding and removing elements from either end. 
The Deque module is a part of collections library. 
It has the methods for adding and removing elements which can be invoked directly with arguments.
"""
import collections
# Create a deque
DoubleEnded = collections.deque(["Mon", "Tue", "Wed"])
print(DoubleEnded)

# Append to the right
print("Adding to the right: ")
DoubleEnded.append("Thu")
print(DoubleEnded)

# append to the left
print("Adding to the left: ")
DoubleEnded.appendleft("Sun")
print(DoubleEnded)

# Remove from the right
print("Removing from the right: ")
DoubleEnded.pop()
print(DoubleEnded)

# Remove from the left
print("Removing from the left: ")
DoubleEnded.popleft()
print(DoubleEnded)

# Reverse the dequeue
print("Reversing the deque: ")
DoubleEnded.reverse()
print(DoubleEnded)
