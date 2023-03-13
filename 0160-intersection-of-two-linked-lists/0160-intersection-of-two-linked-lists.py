# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        tempA = headA
        tempB = headB
        lenA = lenB = 0
        while tempA.next:
            lenA += 1
            tempA = tempA.next

        while tempB.next:
            lenB += 1
            tempB = tempB.next  

        if tempA != tempB:
            return None    

        if lenA > lenB:
            travx = headA
            travy = headB
        else:
            travx = headB
            travy = headA

        cnt = 0
        while travx:
            if cnt >= abs(lenA - lenB):
                if travx == travy:
                    return travx
                travy = travy.next    
            travx = travx.next
            cnt += 1

