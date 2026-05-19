# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # return  [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right) if root else []
        # iterative
        stck = []
        preorder = []
        temp = root
        # while True:
        #     if temp:
        #         preorder.append(temp.val)
        #         stck.append(temp)
        #         temp = temp.left
        #     else:
        #         if not stck:
        #             return preorder
        #         temp = stck.pop()
        #         temp = temp.right
        while stck or temp:
            while temp:
                preorder.append(temp.val)
                stck.append(temp)
                temp = temp.left
            if stck:
                node = stck.pop()
                temp = node.right
        return preorder


        