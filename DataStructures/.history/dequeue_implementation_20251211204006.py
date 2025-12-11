class Dequeue:
    def __init__(self):
        self.dequeue = []

    def isEmpty(self):
        return len(self.dequeue) == 0

    def isFull(self):
        return len(self.dequeue) == 10

    def add_at_start(self, data):
        if not self.isFull():
            # insert at the beginning
            self.dequeue.insert(0, data)
        else:
            print("The Dequeue Container is Full")

    def add_at_end(self, data):
        if not self.isFull():
            # append at the end
            self.dequeue.append(data)
        else:
            print("The Dequeue Container is Full")

    def remove_at_start(self):
        if not self.isEmpty():
            # remove and return first element
            return self.dequeue.pop(0)
        else:
            print("The Dequeue Container is Empty")

    def remove_at_end(self):
        if not self.isEmpty():
            # remove and return last element
            return self.dequeue.pop()
        else:
            print("The Dequeue Container is Empty")

    def show(self):
        print(self.dequeue)


if __name__ == "__main__":
    dq = Dequeue()

    print("Is empty at start?", dq.isEmpty())  # True

    print("\nAdd at end: 10, 20")
    dq.add_at_end(10)      # [10]
    dq.add_at_end(20)      # [10, 20]
    dq.show()

    print("\nAdd at start: 5, 1")
    dq.add_at_start(5)     # [5, 10, 20]
    dq.add_at_start(1)     # [1, 5, 10, 20]
    dq.show()

    print("\nRemove at start:")
    removed = dq.remove_at_start()   # removes 1
    print("Removed:", removed)
    dq.show()                        # [5, 10, 20]

    print("\nRemove at end:")
    removed = dq.remove_at_end()     # removes 20
    print("Removed:", removed)
    dq.show()                        # [5, 10]

    print("\nFill up to capacity...")
    dq.add_at_end(30)
    dq.add_at_end(40)
    dq.add_at_end(50)
    dq.add_at_end(60)
    dq.add_at_end(70)
    dq.add_at_end(80)
    dq.add_at_end(90)  
    dq.add_at_start(15)   
    dq.add_at_start(1) 
    dq.add_at_end(100)   
    dq.show()
    print("Is full?", dq.isFull())
