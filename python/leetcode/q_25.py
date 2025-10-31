# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # Standard linked list reversal function (reverses list from 'start' up to 'end' (exclusive))
    def reverse_segment(self, start: ListNode, end: ListNode) -> ListNode:
        prev = None
        curr = start
        while curr != end:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev # This is the new head of the reversed segment

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head

        dummy = ListNode(0, head)
        pre = dummy
        
        while pre:
            # 1. Check if k nodes exist
            curr = pre
            for _ in range(k):
                if not curr.next: # Not enough nodes left
                    return dummy.next
                curr = curr.next
            
            # Now 'curr' is the k-th node in the list (the end of the segment)
            
            # 'start' is the first node of the group
            start = pre.next 
            # 'next_group_head' is the node immediately after the k-group
            next_group_head = curr.next 
            
            # 2. Reverse the k-group
            # We use start and next_group_head to define the segment
            new_head = self.reverse_segment(start, next_group_head)
            
            # 3. Reconnect the reversed group
            
            # Connect the previous part to the new head
            pre.next = new_head
            
 

        return dummy.next