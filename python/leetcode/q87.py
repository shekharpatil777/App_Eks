class Solution:
    def __init__(self):
        self.memo = {}

    def isScramble(self, s1: str, s2: str) -> bool:
        # Check memoization table
        if (s1, s2) in self.memo:
            return self.memo[(s1, s2)]
        
        # Base Case: Strings are identical
        if s1 == s2:
            return True
        
        # Pruning: If characters don't match, they can't be scrambles
        if sorted(s1) != sorted(s2):
            return False
        
        n = len(s1)
        for i in range(1, n):
            # Case 1: Left matches Left, Right matches Right (No swap at this level)
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                self.memo[(s1, s2)] = True
                return True
            
