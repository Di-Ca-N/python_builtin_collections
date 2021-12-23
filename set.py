s = {1, 1, 1 , 2, 3, 4, 5, 6}
print(s)

# O(1)
1 in s       # Check membership
s.add(7)     # Add element
s.pop()      # Pop element
s.remove(1)  # Remove element
s.discard(1) # Remove element (if it is a member)
len(s)       # Len

# O(n)
s.clear() # Clear set
s.copy()  # Copy set
