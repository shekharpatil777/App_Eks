import collections

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def closestKValues(self, root: TreeNode | None, target: float, k: int) -> list[int]:
        dq = collections.deque()
        
        # In-order traversal to get the nodes in sorted order
        def inorder(node: TreeNode | None) -> None:
            if not node:
                return
            inorder(node.left)
            dq.append(node.val)
            inorder(node.right)
                
        inorder(root)

        
        # Shrink the deque to exactly k elements using a sliding window
        while len(dq) > k:
            if abs(dq[0] - target) > abs(dq[-1] - target):
                dq.popleft()
            else:
                dq.pop()
                
        return list(dq)