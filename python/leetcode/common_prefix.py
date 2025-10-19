from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        # Start with the first string as the initial prefix
        prefix = strs[0]
        
        # Iterate over the rest of the strings
        for i in range(1, len(strs)):
            current_string = strs[i]
            
            # While the current string does NOT start with the current prefix,
            # shorten the prefix by one character from the end.
            # The str.startswith() method is convenient for this.
            while not current_string.startswith(prefix):
                # Shorten the prefix by removing the last character
                prefix = prefix[:-1]
                

                    
        return prefix