# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def leaves(root, arr):
            if not root:
                return
            if not root.left and not root.right:
                arr.append(root.val)
            leaves(root.left, arr)
            leaves(root.right, arr)
        l1 = []
        l2 = []
        leaves(root1, l1)
        leaves(root2, l2)
        
        if len(l1) != len(l2):
            return False
        
        for i in range(0, len(l1)):
            if l1[i] != l2[i]:
                return False
        return True
            
        