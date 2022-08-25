# Basic Data Structures

from collections import deque
from queue import LifoQueue

# Stack
list_stack = []
deque_stack = deque()
lifo_stack = LifoQueue()


# grow and shrink
list_stack.append(27)
print(list_stack.pop())

deque_stack.append(27)
print(deque_stack.pop())

lifo_stack.put(27)
print(lifo_stack.get())

# Convert stack [3, 4, 6, 7] into [3, 4, 8, 9]
list_stack.append(3)
list_stack.append(4)
list_stack.append(6)
list_stack.append(7)
print(list_stack)
