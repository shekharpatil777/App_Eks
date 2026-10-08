import random
from collections import defaultdict

class RandomizedCollection:

    def __init__(self):
        # Maps a value to a set of its indices in the self.values list
        self.val_to_indices = defaultdict(set)
        # Stores the actual values to allow random.choice in O(1)
        self.values = []

    def insert(self, val: int) -> bool:
        """Inserts a value to the collection. Returns true if the collection did not already contain the specified element."""
        # Check if the value is not already in the collection (set is empty)
        not_present = not self.val_to_indices[val]
        
        # Add the new index to the set for this value
        self.val_to_indices[val].add(len(self.values))
        # Append the value to the array
        self.values.append(val)
        
        return not_present

    def remove(self, val: int) -> bool:
        """Removes a value from the collection. Returns true if the collection contained the specified element."""
        if not self.val_to_indices[val]:
            return False
        
        # 1. Get an arbitrary index of the value to remove, and the last value in the array
        idx_to_remove = self.val_to_indices[val].pop()
        last_val = self.values[-1]
        
        # 2. Swap the last value into the spot of the value we are removing
        self.values[idx_to_remove] = last_val
        
        # 3. Update the index set for the last value
        self.val_to_indices[last_val].add(idx_to_remove)
        self.val_to_indices[last_val].discard(len(self.values) - 1)
        
        # 4. Remove the last element from the array
        self.values.pop()
        
        return True

    def getRandom(self) -> int:
        """Get a random element from the current collection of elements."""
        return random.choice(self.values)