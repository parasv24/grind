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
        curr = root
        while curr:
            if not curr.left:
                curr = curr.right
            else:
                temp = curr.left
                while temp.right and temp.right != curr.right:
                    temp = temp.right
                if temp.right != curr.right:
                    temp.right = curr.right
                prev = curr.left
                curr.left = None
                curr.right = prev
                curr = prev
                
                
        
