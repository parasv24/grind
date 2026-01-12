# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def length(head):
            if not head:
                return 0
            return 1 + length(head.next)
        newn = length(head) - n + 1
        # print(newn)
        def remove(head, n):
            if n == 1:
                return head.next

            head.next = remove(head.next, n-1)
            return head
        return remove(head, newn)

        