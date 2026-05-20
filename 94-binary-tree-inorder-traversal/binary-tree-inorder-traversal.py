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

        # stck = []
        # temp = root
        # inorder = []
        # while stck or temp:
        #     while temp:
        #         stck.append(temp)
        #         temp = temp.left
        #     if stck:
        #         node = stck.pop()
        #         inorder.append(node.val)
        #         temp = node.right
        # return inorder

        pre = []
        inorder = []
        post = []

        stck = []
        if root:
            stck.append([root, 1])
        while stck:
            node, val = stck.pop()
            if val == 1:
                pre.append(node.val)
                stck.append([node, 2])
                if node.left:
                    stck.append([node.left, 1])
            elif val == 2:
                inorder.append(node.val)
                stck.append([node, 3])
                if node.right:
                    stck.append([node.right, 1])
            else:
                post.append(node.val)
        return inorder
            