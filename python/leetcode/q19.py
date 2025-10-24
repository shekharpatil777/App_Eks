class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    dummy = ListNode(0, head)
    fast = dummy
    slow = dummy

    # Advance fast by n+1 steps
    for _ in range(n + 1):
        fast = fast.next



    # Delete the n-th node from end
    slow.next = slow.next.next if slow.next else None
    return dummy.next
