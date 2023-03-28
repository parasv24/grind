# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        def inorder(root):
            return inorder(root.left) + [root.val] + inorder(root.right) if root else []
        arr = inorder(root)
        ans = 100000000000000
        for i in range(0, len(arr)-1):
            ans = min(ans, arr[i+1] - arr[i])
        return ans
        