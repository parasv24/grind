# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def form_tree(postorder, inorder):
            if len(postorder) == 1:
                return TreeNode(postorder[0])
            
            root = postorder[-1]
            node = TreeNode(root)
            idx_root = -1
            for i in range(len(inorder)):
                if inorder[i] == root:
                    idx_root = i
                    break
            if idx_root != len(postorder) - 1:
                node.right = form_tree(postorder[idx_root: -1], inorder[idx_root+1: ])
            if idx_root != 0:
                node.left = form_tree(postorder[0: idx_root], inorder[0: idx_root])
            return node
        return form_tree(postorder, inorder) 