"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        ans = []
        def dfs(node):
            if not node:
                return
            ans.append(node)
            if node.child:
                dfs(node.child)
            if node.next:
                dfs(node.next)
        dfs(head)
        prev = None
        for el in ans:
            el.prev = prev
            if prev:
                prev.next = el
            el.child = None
            prev = el
        return head
        