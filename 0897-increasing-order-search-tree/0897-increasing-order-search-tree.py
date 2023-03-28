# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def inorder(root, arr):
            if not root:
                return None
            inorder(root.left, arr)
            arr.append(root.val)
            inorder(root.right, arr)
            return
        ans = []
        inorder(root, ans)
        root = TreeNode(ans[0])
        temp = root
        for i in range(1, len(ans)):
            temp.right = TreeNode(ans[i])
            temp = temp.right
        return root
            
            
        