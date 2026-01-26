class Solution:
    def numTrees(self, n: int) -> int:
        # dp[i] stores the number of unique BSTs with i nodes
        dp = [0] * (n + 1)
        
        # Base cases: 
        # 0 nodes -> 1 empty tree
        # 1 node -> 1 tree
        dp[0], dp[1] = 1, 1
        
        # Fill the DP table for each number of nodes from 2 up to n
        for nodes in range(2, n + 1):
            for root in range(1, nodes + 1):
                # left nodes = root - 1
                # right nodes = nodes - root
                dp[nodes] += dp[root - 1] * dp[nodes - root]
                
        return dp[n]