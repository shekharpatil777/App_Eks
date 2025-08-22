# Create a list
arr = [10, 20, 30, 40]

# Insert element
arr.insert(2, 25)   # [10, 20, 25, 30, 40]

# Delete element
arr.remove(30)      # [10, 20, 25, 40]

# Search element
print(25 in arr)    # True

# Iterate
for val in arr:
    print(val)
