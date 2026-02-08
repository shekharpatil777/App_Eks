# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        # Step 1: get length of linked list
        def get_length(node):
            length = 0
            while node:
                length += 1
                node = node.next
            return length
        
        n = get_length(head)
        self.curr = head
        
        # Step 2: build BST using inorder traversal
        def build(l, r):
            if l > r:
                return None
            
            mid = (l + r) // 2
            
            # build left subtree
            left = build(l, mid - 1)
            
