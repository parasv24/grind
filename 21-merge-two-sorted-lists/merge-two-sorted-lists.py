# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        def merge(a, b):
            if not a:
                return b
            if not b:
                return a
            if a.val < b.val:
                node = merge(a.next, b)
                a.next = node
                return a
            node = merge(a, b.next)
            b.next = node
            return b
        return merge(list1, list2)
        