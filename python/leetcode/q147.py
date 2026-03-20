class Solution:
    def insertionSortList(self, head):
        dummy = ListNode(0)
        curr = head

        while curr:
            prev = dummy
            nxt = curr.next  # store next node

