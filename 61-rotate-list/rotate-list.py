# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        temp = head
        ln = 0
        while temp:
            ln += 1
            if not temp.next:
                # ln += 1
                temp.next = head
                break
            temp = temp.next
        k = k % ln
        cnt = ln - k
        temp = head
        # print(cnt, k, ln)
        prev = None
        while cnt > 0:
            prev = temp
            temp = temp.next
            cnt -= 1
        new_head = head
        if prev:
            new_head = prev.next
            prev.next = None
        return new_head
        
        