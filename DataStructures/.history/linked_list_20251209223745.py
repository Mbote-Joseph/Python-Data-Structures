class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None
        
    def list_print(self):
        print_value = self.head
        while print_value is not None:
            print(print_value.data)
            print_value = print_value.next
        
list1 = SLinkedList()
list1.head = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

# Link. the first Node to the second Node

list1.head.next = e2

# Link Second Node to third Node
e2.next = e3

print(list1.head)

list1.list_print()