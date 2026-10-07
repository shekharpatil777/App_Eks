import random

class RandomizedSet:

    def __init__(self):
        # Maps value to its index in self.values
        self.val_to_index = {}
        # Stores values to allow O(1) random access
        self.values = []

    def insert(self, val: int) -> bool:
        """Inserts a value to the set. Returns true if the set did not already contain the specified element."""
        if val in self.val_to_index:
            return False
            
        # Add to dict with the current length of the array as its index
        self.val_to_index[val] = len(self.values)
        # Append to array
        self.values.append(val)
        return True

    def remove(self, val: int) -> bool:
        """Removes a value from the set. Returns true if the set contained the specified element."""
        if val not in self.val_to_index:
            return False
            
        # Get the index of the element to remove and the value of the last element
        idx_to_remove = self.val_to_index[val]
        last_val = self.values[-1]
        
        # Move the last element to the index of the element being removed
        self.values[idx_to_remove] = last_val
        self.val_to_index[last_val] = idx_to_remove
        
        # Pop the last element from the array and delete the target from the dict
        self.values.pop()
        del self.val_to_index[val]
        
        return True

    def getRandom(self) -> int:
        """Get a random element from the current set of elements."""
        return random.choice(self.values)