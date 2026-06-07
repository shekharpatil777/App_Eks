#test
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Base case: if we hit the bottom of a branch, or find p or q
        if not root or root == p or root == q:
            return root
        
        # Look left and right
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        # If both left and right returned something, the current node is the LCA
        if left and right:
            return root
            
        # Otherwise, return the non-null side (or None if both are None)
        return left if left else right
