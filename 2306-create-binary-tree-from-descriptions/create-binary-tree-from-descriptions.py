# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        mp = {}
        parents = set()
        child = set()
        for x, y, is_l in descriptions:
            nx , ny = mp.get(x, TreeNode(x)), mp.get(y, TreeNode(y))
            mp[x] = nx
            mp[y] = ny
            if is_l:
                nx.left = ny
            else:
                nx.right = ny
            if  nx not in child:
                parents.add(nx)
            if ny in parents:
                parents.remove(ny)
            child.add(ny)
        return parents.pop()