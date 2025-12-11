# Stack

class Stack:
    def __init__(self):
        self.stack = []
        
    def add(self, data):
        if data not in self.stack and not isFull():
            self.stack.append(data)
            return True
        else:
            return False
        
    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        else:
            False
        
    def isFull(self):
        if len(self.stack) == 10:
            return True
        else:
            False
            
my_stack = Stack()
my_stack.add(10)