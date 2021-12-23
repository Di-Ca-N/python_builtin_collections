from collections import deque

dq = deque([1, 2, 3, 4, 5, 6])

# O(1)
dq.append(7)     # Append to the right
dq.appendleft(0) # Append to the left
dq.pop()         # Pop from right
dq.popleft()     # Pop from left

# O(n)
dq.remove(2)  # Remove element
dq[2]         # Get element by index
dq[2] = 3     # Update element at index

dq.copy()     # Copy
dq.clear()    # Clear