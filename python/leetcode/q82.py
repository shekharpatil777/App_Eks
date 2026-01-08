# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        curr = head

        while curr:
            # Detect duplicates
            if curr.next and curr.val == curr.next.val:
                dup_val = curr.val
                # Skip all nodes with dup_val

