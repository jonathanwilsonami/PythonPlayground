## Garbage Collection
- Def: process of finding data objects in a running program that connot be accessed in the future, and to reclaim the resources used by those objects. 
- Reference Cycles/Circlular Reference - Objects A and B reference each other. The GC looks for these and removes them. Uses the reference counter. 
- Python uses reference counting - It can reclaim objects when the rc goes to 0. 
- Tracing - Java uses this. Allows for threading which gives it higher performance. 