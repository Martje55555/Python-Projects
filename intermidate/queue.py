# Queue implementation in Python
class Queue:
    def __init__(self):
        self.queue = []

    # Add an element
    def enqueue(self, item):
        self.queue.append(item)

    # Remove an element
    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    # Display  the queue
    def display(self):
        print(self.queue)

    def size(self):
        return len(self.queue)

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)

print("Original array: ", end="")
q.display()

q.dequeue()

print("After removing an element: ", end="")
q.display()

q.enqueue(6)
print("After adding an item (6): ", end="")
q.display()

print("Getting size of queue: ", q.size())