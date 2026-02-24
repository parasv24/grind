# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def sum(root, cur):
            if not root.left and not root.right:
                return 2 * cur + root.val
            left_ans, right_ans = 0 , 0
            if root.left:
                left_ans = sum(root.left, 2 * cur + root.val)
            if root.right:
                right_ans = sum(root.right, 2 * cur + root.val)
            return left_ans + right_ans
        return sum(root, 0)
        