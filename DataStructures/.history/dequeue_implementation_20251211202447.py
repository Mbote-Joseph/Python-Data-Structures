# DEQUEUE - A double-ended queue supports  adding and removing elements from either end. 

class Dequeue:
    def __init__(self):
        self.dequeue = []
        
    def isEmpty(self):
        if len(self.dequeue) == 0:
            return True
        else:
            return False
        
    def isFull(self):
        if len(self.dequeue) == 10:
            return True
        else:
            return False
    
    def add_at_start(self, data):
        if not self.isFull():
            self.dequeue.insert(0, data)
            return self.dequeue
        else:
            print("The Dequeue Container is Full")
        
    def add_at_end(self, data):
        if not self.isFull():
            self.dequeue.append(data)
            return self.dequeue
        else:
            print("The Dequeue Container is Full")
            
    def