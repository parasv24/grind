# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head.next
        prev = head
        ans = 0
        while temp:
            ans += temp.val 
            if temp.val == 0:
                temp.val = ans
                ans = 0
                prev.next = temp
                prev = temp   
            temp = temp.next
        return head.next