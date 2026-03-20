class Solution:
    def insertionSortList(self, head):
        dummy = ListNode(0)
        curr = head

        while curr:
            prev = dummy
            nxt = curr.next  # store next node

            # find correct position
            while prev.next and prev.next.val < curr.val:
                prev = prev.next

            # insert current node
            curr.next = prev.next
            prev.next = curr

            curr = nxt

        return dummy.next