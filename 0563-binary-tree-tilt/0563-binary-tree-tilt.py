# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        fin_ans  = 0
        def solve(root):
            nonlocal fin_ans
            if not root:
                return 0, 0
            ans1, sum1 = solve(root.left)
            ans2, sum2 = solve(root.right)
            fin_ans+= abs(sum1- sum2)
            # print(sum1, sum2,abs(sum1 -sum2) ,ans2)
            return abs(sum1- sum2), sum1 + sum2 + root.val
        ans, _ = solve(root)
        return fin_ans
        
