# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        depths = {}
        parents = {}
        def dep(root, depth, par):
            nonlocal depths
            if not root:
                return
            depths[root.val] = depth
            parents[root.val] = par
            dep(root.left, depth + 1, root.val)
            dep(root.right, depth + 1, root.val)
            
        dep(root, 0, None)
        return depths[x] == depths[y] and parents[x] != parents[y]
            
            
