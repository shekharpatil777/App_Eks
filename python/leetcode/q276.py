class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return k
        
        same = k          # first 2 posts same color
        diff = k * (k - 1)  # first 2 posts different color
