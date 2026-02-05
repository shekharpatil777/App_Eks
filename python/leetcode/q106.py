# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, inorder, postorder):
        # Map value -> index in inorder
        idx_map = {val: i for i, val in enumerate(inorder)}
        
        def helper(left, right):
            if left > right:
                return None
            
            # Last element in postorder is the root
            root_val = postorder.pop()
            root = TreeNode(root_val)
            
            # Index of root in inorder
            index = idx_map[root_val]
            

            # Build right subtree first
            root.right = helper(index + 1, right)
            root.left = helper(left, index - 1)
            
            return root
        
        return helper(0, len(inorder) - 1)
