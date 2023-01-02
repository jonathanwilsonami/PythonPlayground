import sys
sys.path.append(".")
# from PythonPlayground.DataStructures.double_linked_list import dLinkedList
# from PythonPlayground.DataStructures.double_linked_list import dLinkedList

class Node:
    def __init__(self, data):
        self.val = data
        self.next = None

class sLinkedList:
    def __init__(self):
        self.head = None

    def add_item(self, val):
        if self.head is None:
            self.head = Node(val)
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n_new = Node(val)
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
            print("Linked List: []")
        else:
            n = self.head
            display_string = ["Linked List: ["]
            while n is not None:
                display_string.append(f"({n.val})->")
                n = n.next
            display_string.append("None]")
            print(*display_string)        
            print("\n")

    def revmoveElements(self, head, val):
        while head is not None and head.val is val:
            head = head.next
        
        curr_node = head
        while curr_node is not None and curr_node.next is not None:
            if curr_node.next.val is val:
                curr_node.next = curr_node.next.next
            else:
                curr_node = curr_node.next
        
        return(head)
    # def removeElements(self, val):
    #     if self.head is None:
    #         return(self.head)
    #     else: 
    #         if self.head.next is None:
    #             if self.head.val is val:
    #                 self.head = None
    #                 return(self.head)
    #             else:
    #                 return(self.head)
    #         else:
    #             n = self.head
    #             while n is not None:
    #                 tail = n.next
    #                 if tail is not None and tail.val is val:
    #                     n.next = tail.next
    #                 elif n.val is val and n.next is not None:
    #                     next_n = n.next
    #                     n.val = next_n.val
    #                     n.next = next_n.next
    #                 else:
    #                     n = n.next 
    #             n = self.head 
    #             if n.val is val:
    #                 self.head = None
    #             return(self.head)



# Given the head of a linked list and an integer val, 
# remove all the nodes of the linked list that has Node.val == val, and return the new head.

sLL = sLinkedList()
sLL.add_item(6)
sLL.add_item(6)
sLL.add_item(1)
sLL.add_item(6)
sLL.add_item(6)
sLL.add_item(1)
sLL.add_item(7)
sLL.add_item(6)
sLL.display()
sLL.revmoveElements(sLL.head, 6)
sLL.display()
