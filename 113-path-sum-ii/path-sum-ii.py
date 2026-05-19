# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        if not root.left and not root.right and root.val == targetSum:
            return [[root.val]]
        ans = []
        def rec(root, small_ans, val):
            if not root.left and not root.right and val == root.val:
                ans.append(small_ans + [val])
            if root.left:
                rec(root.left, small_ans + [root.val] , val - root.val)
            if root.right:
                rec(root.right, small_ans + [root.val], val - root.val)
        if root.left:
            rec(root.left, [root.val], targetSum - root.val)
        if root.right:
            rec(root.right, [root.val], targetSum - root.val)
        return ans


        