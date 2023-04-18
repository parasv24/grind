# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        if not head.next:
            return [0]
        
        def helper(head):
            temp = None
            prev = None
            curr = head
            l = 0
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
                l += 1
            return prev, l
        reverse_list, n = helper(head)
        temp = reverse_list
        stck = []
        ans = [0 for _ in range(n)]
        while n >=0 and temp:
            while len(stck) > 0:
                if stck[-1] <= temp.val:
                    stck.pop()
                else:
                    ans[n-1] = stck[-1]
                    break
            # print(ans)
            stck.append(temp.val)
            n-=1
            temp = temp.next
        return ans