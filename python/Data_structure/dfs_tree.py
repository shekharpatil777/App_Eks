class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)

root = TreeNode(1)
root.left = TreeNode(2)

