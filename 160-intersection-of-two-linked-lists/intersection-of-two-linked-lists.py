# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # 1st method
        # len1, len2 = 0, 0
        # temp1, temp2 = headA, headB
        # while temp1:
        #     len1 += 1
        #     temp1 = temp1.next
        
        # while temp2:
        #     len2 += 1
        #     temp2 = temp2.next
        
        # def get_intersection(a,b,diff):
        #     while diff > 0:
        #         a = a.next
        #         diff -= 1
        #     while a:
        #         if a == b:
        #             return a
        #         a, b = a.next, b.next
        #     return None
        # if len1 > len2:
        #     return get_intersection(headA, headB, abs(len1 - len2))
        # else:
        #     return get_intersection(headB, headA, abs(len1 - len2))
        d1, d2 = headA, headB
        while d1 != d2:
            d1 = headB if d1 is None else d1.next
            d2 = headA if d2 is None else d2.next
        return d1