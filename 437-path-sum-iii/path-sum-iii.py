# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        def rec(root, remain, can_start):
            if not root:
                return 0
            
            ans = 1 if root.val == remain else 0

            # start a new path
            if can_start:
                ans += rec(root.left, targetSum, True)
                ans += rec(root.right, targetSum, True)

            # continue current path
            ans += rec(root.left, remain - root.val, False)
            ans += rec(root.right, remain - root.val, False)

            return ans

        return rec(root, targetSum, True)

            
        