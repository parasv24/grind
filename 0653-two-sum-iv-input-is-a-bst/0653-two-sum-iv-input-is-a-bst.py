# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        mp = {}
        def travs(root):
            nonlocal mp
            if not root:
                return
            mp[root.val] = 1
            travs(root.left)
            travs(root.right)
        travs(root)
        for i in mp.keys():
            if mp.get(k-i, -1) != -1 and i != k-i:
                return True
        return False