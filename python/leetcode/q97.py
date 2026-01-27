class Solution:
    def numTrees(self, n: int) -> int:
        # dp[i] stores the number of unique BSTs for i nodes
        dp = [0] * (n + 1)
        dp[0], dp[1] = 1, 1
        
