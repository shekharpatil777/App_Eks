# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []
        
        def build(start, end):
            # Base case: if start > end, there are no nodes to form a tree.
            # We return [None] so the nested loops still execute once.
            if start > end:
                return [None]
            
            all_trees = []
            
            # 1. Iterate through every number i to be the root
            for i in range(start, end + 1):
                # 2. Recursively generate all left and right subtrees
                left_subtrees = build(start, i - 1)
                right_subtrees = build(i + 1, end)
                
                # 3. Connect the root 'i' with all combinations of left/right subtrees
                for left in left_subtrees:
                    for right in right_subtrees:
                        root = TreeNode(i)
                        root.left = left
                        root.right = right
                        all_trees.append(root)
                        
            return all_trees

        return build(1, n)