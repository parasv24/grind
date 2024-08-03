# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # nth node from the back is (len - n + 1) th node from beginning and to delete
        # (len - n + 1) node from the beiginning iterate till one less and do that_node.next = that_node.next.next
        slow = fast = head
        length = 0
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            length += 2
        if fast:
            length += 1

        new_n = length - n + 1
        iterate_til = new_n - 1

        dummy = ListNode(0,head)
        it = dummy
        while iterate_til > 0:
            iterate_til -= 1
            it = it.next
        it.next = it.next.next
        return dummy.next

        