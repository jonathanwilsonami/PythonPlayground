# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        if head is None:
            return(head)
        else: 
            if head.next is None:
                if head.val is val:
                    head = None
                    return(head)
                else:
                    return(head)
            else:
                n = head
                while n is not None:
                    tail = n.next
                    if tail is not None and tail.val is val:
                        n.next = tail.next
                    elif n.val is val and n.next is not None:
                        next_n = n.next
                        n.val = next_n.val
                        n.next = next_n.next
                    else:
                        n = n.next 
                n = head 
                if n.val is val:
                    head = None
                return(head)