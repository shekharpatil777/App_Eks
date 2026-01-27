class Solution:
    def numTrees(self, n: int) -> int:
        # dp[i] stores the number of unique BSTs for i nodes
        dp = [0] * (n + 1)
        dp[0], dp[1] = 1, 1
        
        # Build up from 2 nodes to n nodes
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                # j is the root: left side has j-1 nodes, right side has i-j nodes
                dp[i] += dp[j - 1] * dp[i - j]
        
        return dp[n]
