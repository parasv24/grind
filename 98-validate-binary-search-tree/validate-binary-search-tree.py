# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def in_order(root):
            return in_order(root.left) + [root.val] + in_order(root.right) if root else []
        arr = in_order(root)
        prev = -10 ** 11
        for el in arr:
            if el <= prev:
                return False
            prev = el
        return True