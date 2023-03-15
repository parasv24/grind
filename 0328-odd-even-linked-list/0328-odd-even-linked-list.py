# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next or not head.next.next:
            return head
        
        odd = head
        even = head.next
        even_head = head.next
        while odd.next.next and even.next.next:
            odd.next = odd.next.next
            odd = odd.next
            # print(odd.val)
            even.next = even.next.next
            even = even.next
            # print(even.val)
        
        # print("out of loop")
        # print(odd, even)
        if odd and odd.next and odd.next.next:
            odd.next = odd.next.next
            odd = odd.next
        # print(odd, even)    
        if even and even.next and even.next.next:
            even.next = even.next.next
            even = even.next
        even.next = None
        odd.next = even_head
        # print(odd)
        return head