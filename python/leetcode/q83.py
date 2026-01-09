# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Start at the head of the list
        current = head
        
        # Traverse until the end of the list
        while current and current.next:
            if current.val == current.next.val:
