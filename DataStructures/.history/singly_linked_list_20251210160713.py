# Algorithm
# ========== Insertion at the beginning
# 1. START
# 2. Create a node to store the data
# 3. Check if the list is empty
# 4. If the list is empty, add the data to the node and assign the pointer to it.
# 5. It the list is not empty, add the data to a node and link to the current head. Assign the head to the newly added node.
# 6. END


# ============ Insertion at the end
# 1. START
# 2. Create a new node and assign data
# 3. Find the last node
# 4. Point to the last node to the new node
# 5. END

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
      
# Single Linked List which has the head that is then connected to the first Node
class SingleLinkedList:
    def __init__(self):
        self.head = None
    
    # Transverse through the Singly Linked list elements
    def print_linked_list(self):
        node_head = self.head
        while node_head != None:
            print(node_head.data, end="")
            node_head = node_head.next
            if node_head is not None:
                print(" --> ", end="")
            else:
                print()
                
                
    # Inserting an element in the Node
    def insert_element(self, data):
        new_node = Node(data)
        
        new_node.next = self.head
        self.head = new_node
        
    # Inserting at the end of the list. By default insertion takes place at the end on the List
    # def insert_element_at_the_end(self, data):
    #     new_node = Node(data)
    #     if self.head == None:
    #         self.head = new_node
    #         print(new_node)
            
    # Insertion at a given position
    def insert_at_given_position(self, node_at_position, data):
        if node_at_position is None:
            print("The mentioned Node does not exist")
            return
        new_node = Node(data)
        new_node.next = node_at_position.next
        node_at_position.next = new_node
        
    
    def insert_at_position(self, index, data):
        new_node = Node(data)

        # Case 1: inserting at head
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        # Case 2: inserting elsewhere
        current = self.head
        for _ in range(index - 1):
            if current is None:
                raise IndexError("Index out of range")
            current = current.next

        new_node.next = current.next
        current.next = new_node
        
    # Positions - I want to create the node position dynamically without typing head.next.next
    def defining_position(self, index):
        value = "my_list.head"
        for _ in range(index):
            value += ".next"
        return value
    
    # Deletion at the Beginning
    # ============= Algorithm
    # 1. START
    # 2. Assign the head pointer to the next node in the list
    # 3. END
    def deletion_at_the_beginning(self):
        self.head = self.head.next
        
    # Deletion at the End
    # ========== Algorithm
    # 1. START
    # 2. Iterate until you find the second last element in the list.
    # 3. Assign NULL to the send last element in the list.
    # 4. END
    def deletion_at_end(self):
        last_element = self.head.next
        if last_element != None:
            last_element = last_element.next.next 
        last_element.next = None
            

my_list = SingleLinkedList()
my_list.head = Node(0)
my_list.head.next = Node(5)
my_list.head.next.next = Node(10)
my_list.head.next.next.next = Node(15)
my_list.head.next.next.next.next = Node(20)


pos = my_list.head.next.next.next

my_list.insert_element(50)

my_list.insert_at_given_position(pos, 100)
my_list.insert_at_position(1, 440)
my_list.print_linked_list()
my_list.deletion_at_the_beginning()
print("========= After Deletion ========")
my_list.print_linked_list()

print("======= After Deletion at the end")
my_list.deletion_at_end()
my_list.print_linked_list()

print(my_list.defining_position(0))