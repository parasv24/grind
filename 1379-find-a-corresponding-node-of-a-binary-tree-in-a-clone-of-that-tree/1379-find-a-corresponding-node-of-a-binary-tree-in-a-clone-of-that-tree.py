# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if not original:
            return 0
        if original == target:
            return cloned
        ans1 = self.getTargetCopy(original.left, cloned.left, target)
        if ans1:
            return ans1
        ans2 = self.getTargetCopy(original.right, cloned.right, target)    
        if ans2:
            return ans2   


        