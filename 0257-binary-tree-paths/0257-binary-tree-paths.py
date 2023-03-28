# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        def solve(root, s):
            nonlocal ans
            if not root:
                return
            if not root.left and not root.right:
                ans.append((s+"->"+ str(root.val))[2:])
                return
            solve(root.left, s+"->"+ str(root.val))
            solve(root.right, s+"->"+ str(root.val))
        solve(root, "")
        return ans    
            