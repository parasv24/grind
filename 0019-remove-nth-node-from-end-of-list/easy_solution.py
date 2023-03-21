class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast, slow = head, head
        for _ in range(n): fast = fast.next
        if not fast: return head.next
        while fast.next: fast, slow = fast.next, slow.next
        slow.next = slow.next.next
        return head
      
# we can simply stagger our two pointers by n nodes by giving the first pointer (fast) a head start before starting the second pointer (slow). Doing this will cause slow to reach the n'th node from the end at the same time that fast reaches the end.

# Since we will need access to the node before the target node in order to remove the target node, we can use fast.next == null as our exit condition, rather than fast == null, so that we stop one node earlier.

# This will unfortunately cause a problem when n is the same as the length of the list, which would make the first node the target node, and thus make it impossible to find the node before the target node. If that's the case, however, we can just return head.next without needing to stitch together the two sides of the target node.

# Otherwise, once we succesfully find the node before the target, we can then stitch it together with the node after the target, and then return head.
