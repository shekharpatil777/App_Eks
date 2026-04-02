class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None

        ptrA = headA
        ptrB = headB

        # Loop continues until the pointers meet
        while ptrA != ptrB:
            # If ptrA reaches the end, jump to headB, else move to next
            ptrA = ptrA.next if ptrA else headB
            # If ptrB reaches the end, jump to headA, else move to next
            ptrB = ptrB.next if ptrB else headA
            
        return ptrA