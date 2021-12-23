# Stores a sequence of objects. Internally represented as array
l = [4, 1, 2, 3, 5, 7, 8, 2]

# O(1)
l.append(1) # Append element
l.pop()     # Pop last element
l[3]        # Read element at index
l[3] = 0    # Update element at index
len(l)      # Get the len

# O(n)
1 in l      # Check element membership
l.index(1)  # Search an element
l.remove(2) # Remove an element
l.count(2)  # Count appearances of an element

l.insert(3, 10) # Insert elements at the middle
del l[3]        # Delete elements at the middle
l.pop(2)        # Pop elements from the middle

l.copy()  # Copy list
l.clear() # Clear list

# O(n log n)
l.sort()
