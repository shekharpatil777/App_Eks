# Definition for a Node.
# class Node:
#     def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        curr = root
        
        while curr:
            dummy = Node(0)      # Dummy node for next level
            tail = dummy         # Tail pointer to build next level
            
            while curr:
                if curr.left:
                    tail.next = curr.left
                    tail = tail.next
                
                if curr.right:
                    tail.next = curr.right
                    tail = tail.next
                
                curr = curr.next   # Move within current level
            

