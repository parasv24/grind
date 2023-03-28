# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def solve(root):
            if not root:
                return "()"
            if not root.left and not root.right:
                return "(" + str(root.val) + ")"

            ans = "(" + str(root.val)
            ans+= solve(root.left)
            if root.right:
                ans+= solve(root.right)
            return ans + ")"
        temp = solve(root)
        return temp[1:len(temp) - 1]