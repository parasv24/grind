# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        leng = 0
        temp = head
        while temp:
            temp = temp.next
            leng += 1
        k = min(k ,leng - k +1)    
        temp = head
        idx = 0
        while temp:
            if idx == k-1 :
                kth = temp
            if idx == (leng - k):     
                rkth = temp
            idx += 1    
            temp = temp.next
        kth.val , rkth.val = rkth.val , kth.val    
        return head
            