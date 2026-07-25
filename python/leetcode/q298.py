# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
            
        self.max_len = 0
        
        def dfs(node: Optional[TreeNode], parent_val: int, current_len: int) -> None:
            if not node:
                return
            
            # Check if current node extends the consecutive sequence
            if node.val == parent_val + 1:
                current_len += 1
            else:
                current_len = 1
                
            # Update the global maximum length seen so far
            self.max_len = max(self.max_len, current_len)
            
            # Recurse down to left and right children
            dfs(node.left, node.val, current_len)
            dfs(node.right, node.val, current_len)
            
        # Start DFS with the root node. Its parent value is dummy (root.val - 1) 
        # so that the root itself initializes the sequence length to 1.
        dfs(root, root.val - 1, 0)
        
        return self.max_len
