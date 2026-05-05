# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        length = 0
        temp = head
        while temp:
            length += 1
            if not temp.next:
                temp.next = head
                break
            temp = temp.next
        print(length)
        k = k % length
        nodes_to_skip = length - k
        temp = head
        prev = None
        while nodes_to_skip > 0:
            prev = temp
            temp = temp.next
            nodes_to_skip -= 1
        prev.next = None
        return temp
        