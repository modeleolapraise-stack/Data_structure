# NAME: DELE-OSEDELE PRAISE MODELEOLA
# MATRIC NUMBER: 240502041
# COURSE OF STUDY: COMPUTER SCIENCE

class Queue:
    def __init__(self):
        self.queue = []
        self.size = 5

    # Add an element to the queue
    def enqueue(self, item):
        if len(self.queue) == self.size:
            print("Queue Overflow: Queue is full")
        else:
            self.queue.append(item)
            print(item, "added to the queue")

    # Remove an element from the queue
    def dequeue(self):
        if len(self.queue) == 0:
            print("Queue Underflow: Queue is empty")
        else:
            removed = self.queue.pop(0)
            print(removed, "removed from the queue")

    # Display the first element
    def peek(self):
        if len(self.queue) == 0:
            print("Queue is empty")
        else:
            print("Front element:", self.queue[0])

    # Check if the queue is empty
    def is_empty(self):
        return len(self.queue) == 0

    # Check if the queue is full
    def is_full(self):
        return len(self.queue) == self.size

    # Display all elements
    def display(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            print("Queue:", self.queue)


# Create a queue object
q = Queue()

while True:
    print("\nQUEUE OPERATIONS")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Check if Empty")
    print("5. Check if Full")
    print("6. Display")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        item = input("Enter element: ")
        q.enqueue(item)

    elif choice == "2":
        q.dequeue()

    elif choice == "3":
        q.peek()

    elif choice == "4":
        print("Is Empty:", q.is_empty())

    elif choice == "5":
        print("Is Full:", q.is_full())

    elif choice == "6":
        q.display()

    elif choice == "7":
        print("Program terminated")
        break

    else:
        print("Invalid choice")