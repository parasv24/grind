"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        temp = head
        dummy = Node(0)
        new_temp = dummy
        mp = {}
        while temp:
            new_node = Node(temp.val)
            new_temp.next = new_node
            mp[temp] = new_node
            temp = temp.next
            new_temp = new_temp.next
        temp = head
        new_temp = dummy.next
        # print(mp)
        while temp:
            exis_random = temp.random
            new_temp.random = mp.get(exis_random, None)
            temp = temp.next
            new_temp = new_temp.next
        return dummy.next

        
        