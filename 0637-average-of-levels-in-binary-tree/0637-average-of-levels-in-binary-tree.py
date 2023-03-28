# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        def height(root):
            return (max(height(root.left), height(root.right)) + 1) if root else 0
        h = height(root)
        arr = [[0, 0] for _ in range(0,h)]
        def sums(root, depth):
            nonlocal arr
            if not root:
                return
            arr[depth][0]+= root.val
            arr[depth][1]+=1
            sums(root.left, depth + 1)
            sums(root.right, depth + 1)
        sums(root, 0)
        ans = []
        for x, y in arr:
            ans.append(x/y)
        return ans    
        
        