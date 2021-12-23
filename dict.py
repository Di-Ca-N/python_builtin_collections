d = {'1': 1, '2': 2, '3': 3, '4': 4}

# O(1) - Worst case O(n)
d['5'] = 5  # Add key-value pair
d['1']      # Read key
d.get('1')  # Read key
d['1'] += 4 # Update key
del d['1']  # Delete key
'1' in d    # Search key
d.pop('5')  # Pop value by key
d.popitem() # Pop last pair

# O(n)
d.clear()  # Clear dict
d.keys()   # List all keys
d.values() # List all values
d.items()  # List all items
d.copy()   # Copy dict
