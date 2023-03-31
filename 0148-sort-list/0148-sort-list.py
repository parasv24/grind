# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:        
        def merge(list1, list2):
            if not list1:
                return list2
            if not list2:
                return list1
            temp = None
            if list1.val <= list2.val:
                temp = list1
                temp.next = merge(list1.next, list2)
            else:
                temp = list2
                temp.next = merge(list1, list2.next)
            return temp

        def mergeSort(head):
            if  not head or not head.next:
                return head
            slow = head
            fast = head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
                
            new_list = slow.next
            slow.next = None
            list1 = mergeSort(head)
            list2 = mergeSort(new_list)
            sorted_list = merge(list1, list2)
            return sorted_list
        return mergeSort(head)
        