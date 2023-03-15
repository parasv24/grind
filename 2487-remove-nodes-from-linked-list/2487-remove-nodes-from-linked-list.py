# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def reverse(head):
    if head is None or head.next is None:
        return head
    shead = reverse(head.next)
    head.next.next = head
    head.next = None
    return shead

def remove_els(head):
    if head is None or head.next is None:
        return
    
    if head.val > head.next.val:
        head.next = head.next.next
        remove_els(head)
    else:
        remove_els(head.next)
    
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reverse_head = reverse(head)
        remove_els(reverse_head)
        new_head = reverse(reverse_head)
        return new_head