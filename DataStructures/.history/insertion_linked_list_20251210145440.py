# Algorithm
# 1. START
# 2. Create a node to store the data
# 3. Check if the list is empty
# 4. If the list is empty, add the data to the node and assign the pointer to it.
# 5. It the list is not empty, add the data to a node and link to the current head. Assign the head to the newly added node.
# 6. END

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class SingleLinkedList:
    def __init__(self):
        self.head = None
    
    def print_linked_list(self):
        node_head = self.head
        while node_head != None:
            print(node_head.data, end="")
            node_head = node_head.next
            if node_head is not None:
                print("-->", end="")
            else:
                print()

my_list = SingleLinkedList()
my_list.head = Node(0)
my_list.head.next = Node(5)
my_list.head.next.next = Node(10)
my_list.head.next.next.next = Node(15)
my_list.head.next.next.next.next = Node(20)


my_list.print_linked_list()