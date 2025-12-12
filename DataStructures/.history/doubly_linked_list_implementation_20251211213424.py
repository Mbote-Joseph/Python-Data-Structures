class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
        
    
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        
    # Method to add an element at the beginning
    def push(self, new_value):
        NewNode = Node(new_value)
        NewNode.next = self.head
        if self.head is not None:
            self.head.prev = NewNode
        self.head = NewNode
        
    
    # Method to to add elements at the end
    def append(self, new_value):
        NewNode = Node(new_value)
        NewNode.next = None
        if self.head is None:
            NewNode.prev = None
            self.head = NewNode
            return
        last = self.head
        while(last.next is not None):
            last = last.next
        last.next = NewNode
        NewNode.prev = last
        return
    
    # Method to print the list
    def print_list(self, node):
        while (node is not None):
            print(node.data)
            last = node
            node = node.next
            
dl = DoublyLinkedList()
dl.push(12)
dl.append(9)
dl.push(8)
dl.push(62)
dl.append(45)
dl.print_list(dl.head)