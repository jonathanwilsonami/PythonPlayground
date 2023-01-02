# Python supports a type of container dictionaries called “namedtuple()” present in the module, “collections“. Like dictionaries, they contain keys 
# that are hashed to a particular value. But on contrary, it supports both access from key-value and iteration, the functionality that dictionaries lack.

from collections import namedtuple

point = namedtuple('point', 'x,y')

pt = point(1, -4) 
print(pt) # point(x=1, y=-4)
print(pt.x, pt.y) # 1 -4