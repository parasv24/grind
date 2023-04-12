# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(lst1, lst2):
            if not lst1 and not lst2:
                return None
            if not lst1:
                return lst2
            if not lst2:
                return lst1
            head = None
            if lst1.val < lst2.val:
                head = lst1
                lst1 = lst1.next
            else:
                head = lst2
                lst2 = lst2.next
            head.next = merge(lst1, lst2)
            return head
        if not len(lists):
            return
        result = lists[0]
        for i in range(1, len(lists)):
            result = merge(result, lists[i])
        return result
        