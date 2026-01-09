# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        parents = {}
        queue = [root]
        parent = -1
        lvl_traversal = []
        while True:
            temp = []
            lvl_traversal = []
            while len(queue) > 0:
                el = queue.pop()
                lvl_traversal.append(el)
                if el.left:
                    temp.append(el.left)
                    parents[el.left] = el
                if el.right:
                    temp.append(el.right)
                    parents[el.right] = el
            if len(temp) > 0:
                queue = temp
            else:
                break
        if len(lvl_traversal) == 1:
            return lvl_traversal[0]
        # print(lvl_traversal)
        # print(parents[lvl_traversal[0]] == parents[lvl_traversal[1]])
        while True:
            is_ans = True
            for i in range(len(lvl_traversal)):
                lvl_traversal[i] = parents[lvl_traversal[i]]
                if i!= 0 and lvl_traversal[i] != lvl_traversal[i-1]:
                    is_ans = False
            if is_ans or len(lvl_traversal) == 1:
                return lvl_traversal[0]
        return root
