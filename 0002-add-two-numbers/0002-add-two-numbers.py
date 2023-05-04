# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        head = res
        carry = 0
        while l1 and l2:
            sm = l1.val + l2.val + carry
            value = sm % 10
            carry = sm // 10
            res.next = ListNode(value)
            l1 = l1.next
            l2 = l2.next
            res = res.next
        if l1:
            while l1:
                sm = l1.val  + carry
                value = sm % 10
                carry = sm // 10
                res.next = ListNode(value)
                l1 = l1.next
                res = res.next
        if l2:
            while l2:
                sm = l2.val  + carry
                value = sm % 10
                carry = sm // 10
                res.next = ListNode(value)
                l2 = l2.next
                res = res.next
        if carry:
            res.next = ListNode(carry)
        return head.next