class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        self.first = self.second = self.prev = None
        
        def inorder(node):
            if not node:
                return
            
            inorder(node.left)
            
            # Detect the swapped nodes
            if self.prev and node.val < self.prev.val:
                # If first anomaly is found, 'prev' is the suspect
                if not self.first:
                    self.first = self.prev
                # 'node' is always the suspect for the second anomaly
                self.second = node
            
            self.prev = node
            
            inorder(node.right)
        
        inorder(root)

        # Swap the values of the two identified nodes
        self.first.val, self.second.val = self.second.val, self.first.val