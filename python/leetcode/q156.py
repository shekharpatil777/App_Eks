class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        curr = root
        prev = None
        next_node = None
        temp_right = None
        
        while curr:
            next_node = curr.left
            
            # Reassigning the pointers
            curr.left = temp_right
            temp_right = curr.right
            curr.right = prev
            
            # Move to the next level
            prev = curr
            curr = next_node
            
        return prev