# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Handle edge cases: empty list, single node, or no rotation needed (k=0)
        if not head or not head.next or k == 0:
            return head

        # 1. Find the length and the tail of the list
        tail = head
        length = 1
        while tail.next:
            tail = tail.next
            length += 1

        # 2. Convert k to the effective number of rotations
        # Rotation by 'length' brings the list back to its original state.
        effective_k = k % length
        
        # If effective_k is 0, no rotation is needed
        if effective_k == 0:
            return head

        # 3. Form a circle (connect tail to head)
        
        tail.next = head

        # 4. Find the new tail: it is the node (length - effective_k - 1) steps from the original head.
        # This is because the new head will be the node (effective_k) steps *before* the original head.
        # The new tail is the node *before* the new head.
        steps_to_new_tail = length - effective_k - 1
        new_tail = head
        for _ in range(steps_to_new_tail):
            new_tail = new_tail.next

 