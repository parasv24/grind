class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        n1, n2, p = None, None, head
        while p is not None:
            k -= 1
            n2 = None if n2 == None else n2.next
            if k == 0:
                n1 = p
                n2 = head // hum k pe n2 ko head pe point krdenge tonche n-k nodes to traverse and n2 will be automaticlly at n - k
            p = p.next
		# The problem description specifically asks to swap values, not nodes themselves. 
        n1.val, n2.val = n2.val, n1.val
        return head
