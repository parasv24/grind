# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # def rec(left, right):
        #     if not left and not right:
        #         return True
        #     if not left or not right:
        #         return False
            
        #     if left.val != right.val:
        #         return False
        #     return rec(left.right, right.left) and rec(left.left, right.right)
        # return rec(root.left, root.right)
        queue = deque()
        queue.append(root)
        lvl = 0
        while queue:
            if lvl > 0:
                if len(queue) % 2 != 0:
                    return False
                i, j = 0, len(queue) - 1
                while i < j:
                    left , right = queue[i], queue[j]
                    if left or right:
                        flag = True
                    if not left and right:
                        return False
                    if not right and left:
                        return False
                    if left and right and left.val != right.val:
                        return False
                    i += 1
                    j -= 1
            flag = False
            for _ in range(len(queue)):
                node = queue.popleft()
                if node:
                    queue.append(node.left)
                    queue.append(node.right)
                    if node.left or node.right:
                        flag = True
            lvl += 1
            if not flag:
                return True
                
        return True
            
        