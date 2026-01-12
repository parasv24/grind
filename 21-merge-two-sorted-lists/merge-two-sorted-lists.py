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
        # return merge(list1, list2)
        new_head = ListNode()
        temp = new_head
        while list1 and list2:
            if list1.val < list2.val:
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next
            temp = temp.next
        if list1:
            temp.next = list1
        if list2:
            temp.next = list2
        return new_head.next


        