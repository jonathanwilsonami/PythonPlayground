# blocking queue - can elegantly coordinate a pool of producers and a pool of consumers.
# enqueue - adding an ele to a FIFO queue
# dequeue - removing an ele from FIFO queue
# Bounded queue - limit the amount of items in a queue by either rejecting eles that don't fit or overwritting the oldest els
# Examples: internal buffers or caches


from collections import deque

class Queue:
    def __init__(self, *elements):
        self._elements = deque(elements)

    # Make Queue compatible with the len() function
    def __len__(self):
        return len(self._elements)
    
    # Make your class instances usable in a for loop
    def __iter__(self):
        while len(self) > 0:
            yield self.dequeue()

    def enqueue(self, element):
        self._elements.append(element)

    def dequeue(self):
        return self._elements.popleft()
