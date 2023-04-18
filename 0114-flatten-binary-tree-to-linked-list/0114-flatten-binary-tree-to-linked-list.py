# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return 
        
        if not root.left and not root.right:
            return root
        
        left = self.flatten(root.left)
        right = self.flatten(root.right)
        root.right = left
        root.left = None
        temp = root
        while temp.right:
            temp = temp.right
        temp.right = right
        return root    