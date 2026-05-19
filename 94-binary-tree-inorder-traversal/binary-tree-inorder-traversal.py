# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right) if root else []
        # iterative
        # stck = []
        # temp = root
        # inorder = []
        # while True:
        #     if temp is not None:
        #         stck.append(temp)
        #         temp = temp.left
        #     else:
        #         if not stck:
        #             return inorder
        #         temp = stck.pop()
        #         inorder.append(temp.val)
        #         temp = temp.right

        stck = []
        temp = root
        inorder = []
        while stck or temp:
            while temp:
                stck.append(temp)
                temp = temp.left
            if stck:
                node = stck.pop()
                inorder.append(node.val)
                temp = node.right
        return inorder
            