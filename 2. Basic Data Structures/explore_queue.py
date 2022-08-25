# Basic Data Structures

from collections import deque
from queue import Queue

# Stack
list_queue = []
deque_queue  = deque()
lifo_queue  = Queue()


# grow and shrink
list_queue.append(27)
print(list_queue.pop(0))

deque_queue.append(27)
print(deque_queue.popleft())

lifo_queue.put(27)
print(lifo_queue.get())

# Convert stack [2, 8, 3] into [8, 3, 5, 6]
list_queue.append(3)
list_queue.append(4)
list_queue.append(6)
list_queue.append(7)
print(list_queue)
