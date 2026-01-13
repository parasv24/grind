# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def sum(a, b, c):
            if not a and not b:
                if c == 0:
                    return None
                return ListNode(c)
            if not a or not b:
                a = a if a else b
                val = a.val + c
                a.val = val % 10
                a.next = sum(a.next, None, val // 10)
                return a
            val = a.val + b.val + c
            a.val = val % 10
            a.next = sum(a.next, b.next, val // 10)
            return a
        return sum(l1, l2, 0)

