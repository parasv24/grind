# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        dummy = ListNode(-1)
        dummy.next = head
        slow = fast = dummy
        length = 0
        while fast.next and fast.next.next:
            length += 2
            slow = slow.next
            fast = fast.next.next
        if fast.next:
            length += 1

        base_value = length // k
        remainder = length % k
        result = [base_value + 1 if i < remainder else base_value for i in range(k)]
        print(result)
        res = [None] * k
        start = dummy.next
        for i in range(k):
            res[i] = start
            for _ in range(result[i] - 1):
                if start:
                    start = start.next
            if start:
                temp = start.next
                start.next = None
                start = temp
        return res
            

        
        