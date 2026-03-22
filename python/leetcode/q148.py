class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # Base case: if list is empty or has only one node
        if not head or not head.next:
            return head
        
        # 1. Split the list into two halves
        left = head
        right = self.getMid(head)
        tmp = right.next
        right.next = None
        right = tmp
        
        # 2. Recursively sort both halves
        left = self.sortList(left)
        right = self.sortList(right)
        
        # 3. Merge the sorted halves
        return self.merge(left, right)
    
    def getMid(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def merge(self, list1, list2):
        dummy = ListNode()
        tail = dummy
        
