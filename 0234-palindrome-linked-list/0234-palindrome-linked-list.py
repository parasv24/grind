# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def check(self, head):
        if head is None:
            return True

        res = self.check(head.next) and head.val == self.temp.val
        self.temp = self.temp.next
        return res
    
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        self.temp = head
        return self.check(head)
        