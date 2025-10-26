# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = ListNode()  # Dummy node to start the merged list
        tail = dummy



        # Attach the remaining part of the list
        tail.next = list1 if list1 else list2

        return dummy.next
