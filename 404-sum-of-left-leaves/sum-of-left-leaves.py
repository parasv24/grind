# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def get_sum(root, sm , is_left):
            if not root.left and not root.right:
                if is_left:
                    sm += root.val
                return sm
            if root.left:
                sm = get_sum(root.left, sm, True)
            if root.right:
                sm = get_sum(root.right, sm, False)
            return sm
        return get_sum(root, 0 ,False)
        
        