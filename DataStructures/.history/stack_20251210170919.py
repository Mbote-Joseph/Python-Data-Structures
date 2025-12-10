MAX_SIZE = 10
my_stack = [] * MAX_SIZE

def insert(data):
    if len(my_stack) != MAX_SIZE:
        my_stack.push(data)
    else:
        print(f"My stack is full: {my_stack}")
        
def remove():
    data = 0
    if len(my_stack) != 0:
        data = my_stack.pop()
        my_stack
    else:
        print("My Stack is empty")
    return my_stack

insert(12)