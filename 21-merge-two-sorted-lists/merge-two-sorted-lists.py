# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        def merge(a,b):
            if not a:
                return b
            if not b:
                return a
            if a.val < b.val:
                a.next = merge(a.next, b)
                return a
            else:
                b.next = merge(a, b.next)
                return b
        # return merge(list1, list2)
        temp1=list1
        temp2=list2
        head=None

        if temp1 is None:
            return temp2
        if temp2 is None:
            return temp1


        if temp1.val <= temp2.val:
            head=temp1
            temp1=temp1.next
        else:
            head=temp2
            temp2=temp2.next
        ans=head
        while temp1 and temp2:
            if temp1.val <= temp2.val:
                ans.next=temp1
                temp1=temp1.next
            else:
                ans.next=temp2
                temp2=temp2.next
            ans=ans.next
        if temp1:
            ans.next=temp1
        elif temp2:
            ans.next=temp2
        return head
        