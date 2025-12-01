from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Initialize a hash map where the default value is a list
        anagram_groups = defaultdict(list)
        
        for s in strs:
            # 1. Sort the string to create a canonical key.
            # sorted(s) returns a list of characters, so we join them back into a string.
            key = "".join(sorted(s))
            
            # 2. Use the sorted string as the key and append the original string 's'
            anagram_groups[key].append(s)
            
        # 3. Return all the values (the lists of anagrams) from the hash map.
        return list(anagram_groups.values())