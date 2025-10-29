# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swapPairs(head: ListNode) -> ListNode:
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy
    # prev -> first -> second -> following
    while prev.next and prev.next.next:
        first = prev.next
        second = first.next

        # swap
        prev.next = second
        first.next = second.next
        second.next = first

        # move prev two nodes forward
        prev = first

    return dummy.next

