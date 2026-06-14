# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        new_l = None
        temp = head
        length = 0
        while temp:
            nxt = new_l
            new_l = ListNode(temp.val)
            new_l.next = nxt
            temp = temp.next
            length += 1
        length = length // 2
        maxi = 0
        while length > 0:
            maxi = max(maxi, head.val + new_l.val)
            head = head.next
            new_l = new_l.next
            length -= 1
        return maxi

        