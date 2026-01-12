# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # cur = head
        # prev = None
        # temp = head
        # while cur.next:
        #     temp = cur.next
        #     cur.next = prev
        #     prev = cur
        #     cur = temp
        # return cur
        def reverse(head, prev):
            if not head:
                return head
            if not head.next:
                head.next = prev
                return head
            temp = head.next
            head.next = prev
            new_head = reverse(temp, head)
            return new_head
        return reverse(head, None)
        