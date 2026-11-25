"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        curr = head
        
        while curr:
            if curr.child:
                # Find the tail of the child branch
                child_tail = curr.child
                while child_tail.next:
                    child_tail = child_tail.next
                
                # Reconnect child_tail with curr.next
                child_tail.next = curr.next
                if curr.next:
                    curr.next.prev = child_tail
