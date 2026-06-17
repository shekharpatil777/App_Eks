from collections import defaultdict
from typing import List

class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        
        def get_key(s):
            if len(s) == 1:
                return ()
            
            key = []
            for i in range(1, len(s)):
                diff = (ord(s[i]) - ord(s[i - 1])) % 26
                key.append(diff)
            
            return tuple(key)

        groups = defaultdict(list)

        for s in strings:
            groups[get_key(s)].append(s)

        return list(groups.values())