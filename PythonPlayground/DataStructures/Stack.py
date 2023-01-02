# Stack Implementation using a List - less efficient 
stack = []
stack.append('a')
stack.pop()

class Stack:
    def __init__(self):
        self.stack = []

    def add(self, item):
        self.stack.append(item)

    def is_empty(self):
        if len(self.stack) != 0:
            return(False)
        else:
            return(True)
    
    def size(self):
        return(len(self.stack))

    def top(self):
        return(self.stack[-1])

    def pop(self):
        self.stack.pop()


#### TODO
# Stack Implementation using a Linked List
# Do multi threaded processing with LifoQueue  
# Implment a depth-first search (DFS)