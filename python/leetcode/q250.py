# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def countUnivalSubtrees(self, root):
        self.count = 0

        def dfs(node):
            if not node:
                return True

            left = dfs(node.left)
            right = dfs(node.right)

            if not left or not right:
                return False

            if node.left and node.left.val != node.val:
                return False
