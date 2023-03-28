# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if root.val == 2:
            ans1 = self.evaluateTree(root.left)
            ans2 = self.evaluateTree(root.right)
            return ans1 or ans2
        elif root.val == 3:
            ans1 = self.evaluateTree(root.left)
            ans2 = self.evaluateTree(root.right)
            return ans1 and ans2
        else:
            return root.val
        