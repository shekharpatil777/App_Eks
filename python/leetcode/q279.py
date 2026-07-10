class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] + [float('inf')] * n
