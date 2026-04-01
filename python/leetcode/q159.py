class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        n = len(s)
        if n < 3:
            return n
        
        # Hash map to keep track of the rightmost position of characters
        hashmap = {}
        
        max_len = 2
        left = 0
        right = 0
        
        while right < n:
            # Add character and its last seen index to the map
            hashmap[s[right]] = right
            right += 1
            
            # If we have 3 distinct characters, shrink the window
            if len(hashmap) == 3:
                # Find the character with the smallest index (the one to delete)
                del_idx = min(hashmap.values())
                # Remove it from the map
                del hashmap[s[del_idx]]
                # Move left pointer to start a new valid window
                left = del_idx + 1

            
            # Update the maximum length found so far
            max_len = max(max_len, right - left)
            
        return max_len