# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # Dummy nodes to track the start of our two lists
        before_head = ListNode(0)
        after_head = ListNode(0)
        
        # Pointers to move through the two lists
        before = before_head
        after = after_head
        
