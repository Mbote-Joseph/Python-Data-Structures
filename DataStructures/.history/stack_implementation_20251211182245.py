# Stack

class Stack:
    def __init__(self):
        self.stack = []
        
    def add(self, data):
        if data not in self.stack and not self.isFull():
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
            
    def print_stack(self):
        if self.isEmpty():
            print("The Stack is Empty")
        else:
            print(self.stack)
            
    def peek(self):
        if self.isEmpty():
            print("The stack is Empty")
        else:
            return self.stack[-1]
    
    
my_stack = Stack()
my_stack.print_stack()
my_stack.add(10)
my_stack.add(20)
my_stack.add(10)
my_stack.add(30)
my_stack.add(90)
my_stack.add(40)
my_stack.add(50)
my_stack.add(80)

my_stack.print_stack()
