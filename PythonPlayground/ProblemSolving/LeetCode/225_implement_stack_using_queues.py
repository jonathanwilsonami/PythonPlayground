import collections
class MyStack(object):

    def __init__(self):
        self.stack = collections.deque()

    def push(self, x):
        self.stack.append(x)
        

    def pop(self):
        el = self.stack[-1]
        self.stack.pop()
        return(el)
        

    def top(self):
        return(self.stack[-1])
        

    def empty(self):
        return(len(self.stack) == 0)

# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()