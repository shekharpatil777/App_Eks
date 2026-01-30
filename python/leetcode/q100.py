class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.first = None
        self.second = None
        self.prev = TreeNode(float('-inf'))
        
        def inorder(node):
            if not node:
                return
            
            inorder(node.left)
            
            # Detect the swapped nodes
            if self.prev.val > node.val:
                # If it's the first time we find a drop, 
                # 'first' is the previous node
                if not self.first:
                    self.first = self.prev
                # 'second' is always the current node in the drop
                self.second = node
            
            self.prev = node
            
            inorder(node.right)
        
        inorder(root)
        
