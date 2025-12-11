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
