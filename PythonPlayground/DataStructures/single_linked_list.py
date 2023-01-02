class Node:
    def __init__(self, data):
        self.item = data
        self.next = None

class sLinkedList:
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
            n_new.next = None
    
    def pop(self):
        if self is None or self.head is None:
            return(None)
        if self.head.next is None:
            self.head = None
            return
        n = self.head
        new_tail = n
        while n.next is not None:
            new_tail = n
            n = n.next
        new_tail.next = None
        

    def display(self):
        if not self:
            print("The list does not exist")
        elif self.head is None:
            print("[]")
        else:
            n = self.head
            display_string = ["["]
            while n is not None:
                display_string.append(f"({n.item})->")
                n = n.next
            display_string.append("None]")
            print(*display_string)        
            print("\n")

    # TODO
    def removeElements(self, val):
        if self.head is None:
            return([])
        else: 
            if self.head.next is None:
                if self.head.item is val:
                    return([])
                else:
                    return([self.head.item])
            else:
                n = self.head
                res = []
                while n.next is not None:
                    if n.item is not val:
                        res.append(n.item)
                    n.next 
                return(res)

myDoubleLinked = sLinkedList()
myDoubleLinked.display() # []
print(myDoubleLinked.removeElements(6)) # []

myDoubleLinked.add_item(6)
print(myDoubleLinked.removeElements(6)) # []
myDoubleLinked.pop()

myDoubleLinked.add_item(1)
print(myDoubleLinked.removeElements(6)) # [1]
myDoubleLinked.pop()
myDoubleLinked.display()

myDoubleLinked.add_item(1)
myDoubleLinked.add_item(2)
myDoubleLinked.add_item(6)
myDoubleLinked.add_item(3)
myDoubleLinked.add_item(4)
myDoubleLinked.add_item(5)
myDoubleLinked.add_item(6)
myDoubleLinked.display()
print(myDoubleLinked.removeElements(6)) # [ (1)-> (2)-> (3)-> (4)-> (5)-> None]
myDoubleLinked.display()