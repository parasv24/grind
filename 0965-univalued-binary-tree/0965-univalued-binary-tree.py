# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        val = root.val
        def solve(root, val):
            if not root:
                return True
            return solve(root.left, val) and solve(root.right, val) and root.val == val
        return solve(root, val)
        