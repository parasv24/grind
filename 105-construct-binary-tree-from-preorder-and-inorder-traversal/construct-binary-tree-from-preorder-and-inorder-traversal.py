# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def form_tree(preorder, inorder):
            if len(preorder) == 1:
                return TreeNode(preorder[0])
            
            root = preorder[0]
            node = TreeNode(root)
            idx_root = -1
            for i in range(len(inorder)):
                if inorder[i] == root:
                    idx_root = i
                    break
            if idx_root != len(preorder) - 1:
                node.right = form_tree(preorder[idx_root+1: ], inorder[idx_root+1: ])
            if idx_root != 0:
                node.left = form_tree(preorder[1: idx_root+1], inorder[0: idx_root])
            return node
        return form_tree(preorder, inorder)
        