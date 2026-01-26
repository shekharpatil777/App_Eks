class Solution:
    def numTrees(self, n: int) -> int:
        # dp[i] stores the number of unique BSTs with i nodes
        dp = [0] * (n + 1)
        
        # Base cases: 
        # 0 nodes -> 1 empty tree
        # 1 node -> 1 tree
        dp[0], dp[1] = 1, 1
        
