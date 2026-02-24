class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Initialize with a very small number
        self.max_sum = float('-inf')

        def get_max_gain(node):
            if not node:
                return 0

            # Recursively get the max sum from left and right subtrees
            # If the gain is negative, we ignore it (take 0)
            left_gain = max(get_max_gain(node.left), 0)
            right_gain = max(get_max_gain(node.right), 0)

            # This is the price of the path with the current node as the "highest" point (the split)
            current_path_sum = node.val + left_gain + right_gain

            # Update the global maximum if the current path is better
            self.max_sum = max(self.max_sum, current_path_sum)


            # Return the max gain this node can contribute to its parent
            # (We can only pick ONE branch to continue the path)
            return node.val + max(left_gain, right_gain)

        get_max_gain(root)
        return self.max_sum