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
        # return sum(l1, l2, 0)
        c = 0
        new_head = ListNode(0, l1)
        prev = new_head
        while l1 and l2:
            val = l1.val + l2.val + c
            l1.val = val % 10
            c = val // 10
            prev.next = l1
            prev = prev.next
            l1 = l1.next
            l2 = l2.next
        if not l1:
            l1 = l2
        while l1 or c > 0:
            if not l1:
                prev.next = ListNode(c)
                break
            else:
                val = l1.val + c
                l1.val = val % 10
                c = val // 10
                prev.next= l1
                prev = prev.next
                l1 = l1.next
        return new_head.next

            




