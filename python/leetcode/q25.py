# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # Create a dummy node that points to the head of the list.
        # This makes it easier to handle the head swap.
        dummy = ListNode(0)
        dummy.next = head
        
        # 'prev' points to the node right before the pair to be swapped.
        prev = dummy
        
        while prev.next and prev.next.next:
            # Nodes to be swapped: first and second
            first = prev.next
            second = prev.next.next
            
            # Perform the swap:
            
            # 1. 'first' node now points to the node *after* 'second'.
            first.next = second.next
            
            # 2. 'second' node is placed at the current position, 
            #    pointing to 'first'.
            second.next = first
            
 
        return dummy.next