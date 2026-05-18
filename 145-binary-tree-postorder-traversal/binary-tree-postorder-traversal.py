# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val] if root else []
        # iterative
        stck = []
        postorder = []
        temp = root
        while True:
            if temp:
                postorder.append(temp.val)
                stck.append(temp)
                temp = temp.right
            else:
                if not stck:
                    return postorder[::-1]
                temp =stck.pop()
                temp = temp.left
        
        