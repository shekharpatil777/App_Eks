class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        curr = root
        
        while curr or stack:
            # Reach the leftmost node of the current node
            while curr:
                stack.append(curr)
                curr = curr.left
            
            # Backtrack from the stack
            curr = stack.pop()
            res.append(curr.val)
            
