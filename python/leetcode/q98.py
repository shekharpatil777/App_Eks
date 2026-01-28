class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, low=-float('inf'), high=float('inf')):
            # An empty tree is a valid BST
            if not node:
                return True
            
            # The current node's value must be between low and high
            if not (low < node.val < high):
                return False
            
            # Recursively check subtrees with updated ranges
            return (validate(node.left, low, node.val) and 
                    validate(node.right, node.val, high))

        return validate(root)