***************************************************************************
Data Structures in Python
***************************************************************************

Array and List 
==========================================

List and array 

The items are stored in neighboring (contiguous) memory locations.

list.sort() - method employs an algorithm called Timsort, which has O(n log(n)) worst-case time complexity.

Patterns: 
- Deleting from the back instead of the back can be faster
- Create two pointers while moving elements around 


Dictionary (associative array or hashmap) 
==========================================


Linked List (single and double)
==========================================


Stack and Deque 
==========================================

Stack

Stack Methods: 
empty() – Returns whether the stack is empty – Time Complexity: O(1)
size() – Returns the size of the stack – Time Complexity: O(1)
top() / peek() – Returns a reference to the topmost element of the stack – Time Complexity: O(1)
push(a) – Inserts the element at the top of the stack – Time Complexity: O(1)
pop() – Deletes the topmost element of the stack – Time Complexity: O(1)

Uses cases of stacks: 
- keep track of the visited nodes in a graph or a tree traversed with the depth-first search (DFS) algorithm.
- call stacks
- graph traversal algorithms
- language parsing 
- runtime memory management

Deque 

Python's deque objects are implemented as doubly-linked lists, which gives them excellent and consistent performance for 
inserting and deleting elements but poor O(n) performance for randomly accessing elements in the middle of a stack. In Python 
you can access a deque using the collections module.  

Deque is more efficient than using a list when it comes to append and pop opporations because inserting or removing from a list always 
requires a shift of the remaining elements, resulting in a linear, or O(n), time complexity
Lists also occasionally require copying all elements to a new memory location when their number exceeds a certain threshold.
Lists are much better for random-access and fixed-length operations, including slicing, while deques are much more useful for 
pushing and popping things off the ends. List is also not thread-safe. Use LifoQueue for multi threading. See LifoQueue. 

Deque Methods: 
pop()
popleft()
append()
appendleft()
import collections
my_deque = collections.deque([1,2,3])

Deque Use cases: 
- calculating the moving average of pixel intensities in a scan line of a raster image
- a load balancer 
- a task scheduler working in a round-robin fashion 
- store recently opened files, allow a user to undo and redo their actions
- let the user navigate back and forth through their web browsing history.


Queues  
==========================================

Priority Queue

You can think of a priority queue as a list that needs to be sorted every time a new element arrives so that you'll be 
able to remove the last one with the highest priority when performing the dequeue operation. 

LifoQueue 

The LifoQueue stack implementation in the Python standard library is synchronized and provides locking semantics to 
support multiple concurrent producers and consumers.


Graphs and Trees
==========================================


# To know

*Arrays/Lists 
Queues
- Stack
- Priority Queue 
- Deque  
*Hash Table 
Trees and Graphs 
- Tries 
- Undirected Graph 
- Directed Graph
*- Binary 
- AVL Tree 
- Balanced Tree 
- N-ary Tree 
Double and single linkedlists  