# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head.next
        prev = None
        
        while fast.next:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
            fast = fast.next.next
        
        if fast:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        # print(fast,slow,prev)    
        fast, slow = slow   , prev
        m = -1
        while slow and fast:
            m = max(m, slow.val + fast.val)
            slow = slow.next
            fast = fast.next
         
        return m
            
        