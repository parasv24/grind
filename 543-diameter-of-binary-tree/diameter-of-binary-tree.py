# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxi = 0
        def rec(root):
            nonlocal maxi
            if not root:
                return 0
            left = rec(root.left)
            right = rec(root.right)
            maxi = max(maxi, left + right)
            return max(left, right) + 1
        rec(root)
        return maxi
            
        