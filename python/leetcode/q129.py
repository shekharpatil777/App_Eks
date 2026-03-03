class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, current_sum):
            if not node:
                return 0
            
            # Calculate the number represented by the path so far
            current_sum = current_sum * 10 + node.val
            
