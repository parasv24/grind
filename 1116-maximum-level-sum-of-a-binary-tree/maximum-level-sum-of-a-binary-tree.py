# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        ans , cur_max = -1, -10000000
        level = 1
        while len(queue) > 0:
            cur = 0
            temp = deque()
            while len(queue) > 0:
                node = queue.popleft()
                cur += node.val
                if node.right:
                    temp.append(node.right)
                if node.left:
                    temp.append(node.left)
            queue = temp
            if cur > cur_max:
                ans = level
                cur_max = cur
            level += 1
        return ans



        