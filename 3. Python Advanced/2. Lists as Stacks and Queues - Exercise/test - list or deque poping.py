from collections import deque
import time

# Test data
n = 10_000_000
lst = list(range(n))
dq = deque(range(n))

# Timing pop from the end of a list
start = time.time()
for item in reversed(lst):
    lst.pop(item)
list_time = time.time() - start

# Timing pop from the end of a deque
start = time.time()
while dq:
    dq.pop()
deque_time = time.time() - start

print(f"List pop time: {list_time:.6f} seconds")
print(f"Deque pop time: {deque_time:.6f} seconds")
