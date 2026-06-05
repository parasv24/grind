# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        @cache
        def steal(root, can_steal):
            if not root:
                return 0
            ans = 0
            ans = steal(root.left, True) + steal(root.right, True)
            if can_steal:
                ans = max(ans, root.val + steal(root.left, False) + steal(root.right, False))
            return ans
        return max(steal(root, True), steal(root, False))

                
        