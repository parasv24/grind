# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        temp = list1
        cnt = 0;
        while temp:
            if cnt == a-1:
                t1 = temp
            if cnt == b:
                t2 = temp.next
            cnt += 1    
            temp = temp.next
            
        t1.next = list2
        temp2 = list2
        while temp2.next:
            temp2= temp2.next

        temp2.next = t2
        return list1