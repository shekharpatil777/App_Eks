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
        
        curr = head
        while curr:
            if curr.val < x:
                # Add to the "before" list
                before.next = curr
                before = before.next
            else:
                # Add to the "after" list
                after.next = curr
                after = after.next
            
            curr = curr.next
        
        # Important: Terminate the "after" list to prevent cycles
        after.next = None
        
        # Connect the end of "before" to the start of "after"
        before.next = after_head.next
        
        return before_head.next
