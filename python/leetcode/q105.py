class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode:
        # Map values to their indices for O(1) lookup
        in_map = {val: i for i, val in enumerate(inorder)}
        
        def helper(pre_start, in_start, in_end):
            # Base case: if there are no elements to construct the tree
            if in_start > in_end:
                return None
            
            # 1. Pick the current root from preorder
            root_val = preorder[pre_start]
            root = TreeNode(root_val)
            
            # 2. Find where this root is in inorder to split left/right
            root_idx = in_map[root_val]
            
            # 3. Calculate how many nodes are in the left subtree
            left_size = root_idx - in_start
            
            # 4. Recursively build left and right subtrees
            # Left child: next element in preorder is the root
            root.left = helper(pre_start + 1, in_start, root_idx - 1)
            

            # Right child: skip the root and all left subtree nodes in preorder
            root.right = helper(pre_start + left_size + 1, root_idx + 1, in_end)
            
            return root
            
        return helper(0, 0, len(inorder) - 1)