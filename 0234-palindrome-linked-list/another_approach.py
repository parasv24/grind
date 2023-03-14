class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast, prev = head, head, None
        // Finding mid and reversing first half in one go 
        while fast and fast.next:
            fast = fast.next.next
            next = slow.next
            slow.next = prev
            prev = slow
            slow = next
        if fast:
            slow = slow.next
        slow, fast = prev, slow
        while slow and fast:
            if slow.val != fast.val: return False
            slow = slow.next
            fast = fast.next
        return not slow and not fast
