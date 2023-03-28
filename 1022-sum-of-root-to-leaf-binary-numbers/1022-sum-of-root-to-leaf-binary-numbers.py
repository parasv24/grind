# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        self.output = 0
        def solve(root, ans):
            if not root:
                return
            if not root.left and not root.right:
                self.output += (2 * ans + root.val)
                return
            solve(root.left, 2 * ans + root.val)
            solve(root.right, 2 * ans + root.val)
        solve(root, 0)    
        return self.output
        