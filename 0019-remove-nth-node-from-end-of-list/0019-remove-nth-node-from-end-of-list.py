# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None
        leng = 2
        fast = head.next
        slow = head
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            leng += 2
        if fast and fast.next:
            slow = slow.next
            leng += 1
        
        if n == leng:
            head = head.next
            return head
        
        print(leng)
        if (leng // 2) >= n:
            print("eureka")
            z = ((leng // 2) - n)
            while z:
                slow = slow.next
                z -= 1
            print(slow)    
            if slow.next: 
                slow.next = slow.next.next
        else:
            slow = head
            z = leng - n - 1
            while z:
                slow = slow.next
                z -= 1
            if slow.next:    
                slow.next = slow.next.next
        return head   