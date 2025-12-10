class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class SingleLinkedList:
    def __init__(self):
        self.head = None
        
    def print_list(self):
        while self.head != None:
            print(self.head.data, end="")
            self.head = self.head.next
            if self.head != None:
                print("--|\n", end="")
            
        
        

list1 = SingleLinkedList()
list1.head = Node(0)
list1.head.next = Node(5)
list1.head.next.next = Node(10)
list1.head.next.next.next = Node(15)
list1.head.next.next.next.next = Node(20)

list1.print_list()