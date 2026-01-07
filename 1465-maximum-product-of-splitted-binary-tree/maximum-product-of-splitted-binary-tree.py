# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        def sm(root):
            ans  = root.val
            if root.left:
                ans+= sm(root.left)
            if root.right:
                ans += sm(root.right)
            return ans
        total = sm(root)
        mx = -1
        # print(total)
        def rec(root, mx):
            ans  = root.val
            mx1, mx2 = -1, -1
            if root.left:
               a,mx1 = rec(root.left, mx)
               ans += a
            if root.right:
               a,mx2 = rec(root.right, mx)
               ans += a
            # print(ans, total - ans, mx)
            if ans * (total - ans) > mx:
                mx = ans * (total - ans)
            return ans, max([mx, mx1, mx2])
        _ , ans = rec(root, -1)
        return ans % 1000000007

            

        