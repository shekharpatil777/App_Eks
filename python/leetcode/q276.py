class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return k
        
        same = k          # first 2 posts same color
        diff = k * (k - 1)  # first 2 posts different color
        
        for i in range(3, n + 1):
            new_same = diff
            new_diff = (same + diff) * (k - 1)
            
            same = new_same
            diff = new_diff
        
        return same + diff