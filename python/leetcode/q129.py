class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, current_sum):
            if not node:
                return 0
            
            # Calculate the number represented by the path so far
            current_sum = current_sum * 10 + node.val

            # If it's a leaf node, return the accumulated sum
            if not node.left and not node.right:
                return current_sum
            
            # Otherwise, continue down both branches
            return dfs(node.left, current_sum) + dfs(node.right, current_sum)
        
        return dfs(root, 0)            
