# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp, prev = head, None
        while temp:
            next = temp.next
            temp.next = prev
            prev = temp
            if next:
                temp = next
            else:
                break
        return temp
        # def reverse(head, prev):
        #     if not head:
        #         return head
        #     if not head.next:
        #         head.next = prev
        #         return head
        #     temp = head.next
        #     head.next = prev
        #     new_head = reverse(temp, head)
        #     return new_head
        # return reverse(head, None)
        