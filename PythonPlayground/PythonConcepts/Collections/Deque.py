# This is a double ended queue

from collections import deque

d = deque()

d.append(1)
d.append(2)
d.appendleft(3)

print(d)

d.pop()
d.popleft()
d.clear()

print(d) # deque([])

d.extendleft([4,5,6])

print(d) # deque([6, 5, 4])

d.extend([8,9,1])

print(d) # deque([6, 5, 4, 8, 9, 1])

# Rotate 

d.rotate(1) # Rotate elements to right one space
print(d) # deque([1, 6, 5, 4, 8, 9])
 
d.rotate(3) # Rotate elements to right 3 spaces
print(d)

d.rotate(-3) # Rotate elements to left 3 spaces
print(d)