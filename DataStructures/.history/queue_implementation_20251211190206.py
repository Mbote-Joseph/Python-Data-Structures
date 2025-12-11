from stack_implementation import isEmpty
class Queue:
    def __init__(self):
        self.queue = []
        
    def isFull(self):
        if len(self.queue) == 7:
            print("The Queue is Full")
            return True
        else:
            return False
        
    
    def isEmpty(self):
        if len(self.queue) == 0:
            print("The Queue is Empty")
            return True
        else:
            return False
    
    def add(self, data):
        if not self.isFull():
            self.queue.insert(0,data)
            return self.queue
        else:
            print("The Queue is Already Full.")
        
    def remove(self):
        if not self.isEmpty():
            self.queue = self.queue.pop()
            return self.queue
        else:
            print("The Queue is Empty")
    def print_queue(self):
        if self.isEmpty():
            print("The Queue is Empty")
        else:
            print(self.queue)
    
my_queue = Queue()
my_queue.print_queue()
my_queue.add(45)
my_queue.add(55)
my_queue.add(35)
my_queue.add(25)
my_queue.add(145)
my_queue.add(155)
my_queue.add(135)
my_queue.add(125)
my_queue.print_queue()

my_queue.remove()
my_queue.print_queue()
