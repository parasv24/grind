# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def gen_mirror(root):
            if not root:
                return None
            new_node = TreeNode(root.val)
            new_node.right = gen_mirror(root.left)
            new_node.left = gen_mirror(root.right)
            return new_node
        new_root = gen_mirror(root)
        def copies(l, r):
            if not l and not r:
                return True
            if not l or not r:
                return False
            if l.val != r.val:
                return False
            return copies(l.left, r.left) and copies(l.right, r.right)
        return copies(root, new_root)