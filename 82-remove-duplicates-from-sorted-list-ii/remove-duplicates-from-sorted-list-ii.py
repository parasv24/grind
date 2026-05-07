# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        dummy_head = ListNode(-1, head)
        prev_main = dummy_head
        temp = head
        val = head.val
        cnt = 0
        while temp:
            if temp.val == val:
                cnt += 1
            if temp.val != val:
                # print(temp.val, val, cnt, prev.val)
                if cnt == 1:
                    prev_main.next = prev
                    prev_main = prev_main.next
                val = temp.val
                cnt = 1
            prev = temp
            temp = temp.next
        if cnt == 1:
            prev_main.next = prev
            prev_main = prev_main.next
        prev_main.next = None
        return dummy_head.next
        