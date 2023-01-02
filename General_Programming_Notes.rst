## Terms 
- Handle - is an abstract reference to a resource that is used when application software references blocks of memory or objects that are managed 
by another system like a database or an operating system. A resource handle can be an opaque identifier, in which case it is often an integer number 
(often an array index in an array or "table" that is used to manage that type of resource), or it can be a pointer that allows access to further information.
Common resource handles include file descriptors, network sockets, database connections, process identifiers (PIDs), and job IDs. While a pointer contains the 
address of the item to which it refers, a handle is an abstraction of a reference which is managed externally; its opacity allows the referent to be relocated in 
memory by the system without invalidating the handle, which is impossible with pointers. In secure computing terms, because access to a resource via a handle is 
mediated by another system, a handle functions as a capability: it not only identifies an object, but also associates access rights. For example, while a 
filename is forgeable (it is just a guessable identifier), a handle is given to a user by an external system, and thus represents not just identity, but 
also granted access. Like other desktop environments, the Windows API heavily uses handles to represent objects in the system and to provide a communication 
pathway between the operating system and user space. 
- Tape Drives - have to read data sequentially. 
- Disk Drives - allow random access.

*******************************************************
** TODO ***
- Create a testing framework for all code so it can be run and checked
- Package the project up and add reqs 
 
*** TO ADD *** 
Python basics 
- Exception handling 
- Testing

import sys
sys.path.append("/Project/src/")
from PythonPlayground.DataStructures.double_linked_list import dLinkedList
# from ...DataStructures.double_linked_list import dLinkedList

myDoubleLinked = dLinkedList()