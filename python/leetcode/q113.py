class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        results = []
        
        def dfs(node, current_path, current_sum):
            if not node:
                return
            
            # Add current node to the path
            current_path.append(node.val)
            
            # Check if it's a leaf and the sum matches
            if not node.left and not node.right and current_sum == node.val:
                results.append(list(current_path)) # Append a copy of the path
            else:
                # Continue searching left and right
                dfs(node.left, current_path, current_sum - node.val)
                dfs(node.right, current_path, current_sum - node.val)
