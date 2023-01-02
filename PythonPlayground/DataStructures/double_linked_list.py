class Node:
    def __init__(self, data):
        self.item = data
        self.next = None
        self.prev = None

class dLinkedList:
    def __init__(self):
        self.head = None
    
    def add_item(self, item):
        if self.head is None:
            self.head = Node(item)
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n_new = Node(item)
            n.next = n_new
            n_new.prev = n
    
    def pop(self):
        if self.head is None:
            return
        if self.head.next is None:
            del self.head
            return
        n = self.head
        while n.next is None:
            n = n.next
        new_tail = n.prev
        new_tail.next = None  
        del n

    def display(self):
        if self.head is None or not self.head:
            print("The list is empty or does not exist")
            return
        else:
            n = self.head
            display_string = ["None"]
            while n is not None:
                display_string.append(f"<-({n.item})->")
                n = n.next
            display_string.append("None")
            print(*display_string)        
            print("\n")

###############################################################

# TODO 
    # Insert at beginning
    # Display backwards
    # Delete from end 
    # Sort items in list 
    # Find a node
    # Delete node at given position n
    # Reverse doubly linked list
    # Runner TEchnique 
    # Recursion problems
    # Add testing

# Test 
if __name__ == '__main__':

    myDoubleLinked = dLinkedList()

    # Test out add_item
    myDoubleLinked.display()
    # myDoubleLinked.add_item(1)
    # myDoubleLinked.display()
    # myDoubleLinked.add_item(2)
    # myDoubleLinked.display()
    # myDoubleLinked.add_item(3)
    # myDoubleLinked.add_item(4)
    # myDoubleLinked.add_item(5)
    # myDoubleLinked.add_item(6)
    # myDoubleLinked.add_item(7)
    # myDoubleLinked.add_item(8)
    # myDoubleLinked.display()

    # Test out pop
    myDoubleLinked2 = dLinkedList()
    myDoubleLinked2.pop()
    myDoubleLinked2.add_item(1)
    myDoubleLinked2.display()
    myDoubleLinked2.pop()
    myDoubleLinked2.display()
    # myDoubleLinked2.add_item(1)
    # myDoubleLinked2.add_item(2)
    # myDoubleLinked2.display()
    # myDoubleLinked2.pop()
    # myDoubleLinked2.display()



