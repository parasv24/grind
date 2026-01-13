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
        # return remove(head, newn)
        dummy = ListNode(0, head)
        slow, fast = dummy, dummy
        for _ in range(n+1):
            fast = fast.next
        while fast:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy.next

        