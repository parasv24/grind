# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # queue = deque()
        # mp = {}
        # if root:
        #     queue.append(root)
        #     mp[root] = [0, root]
        # while queue:
        #     node = queue.popleft()
        #     level, _ = mp[node]
        #     if node.left:
        #         queue.append(node.left)
        #         mp[node.left] = [level + 1, node]
        #     if node.right:
        #         queue.append(node.right)
        #         mp[node.right] = [level + 1, node]
        # l1, _ = mp[p]
        # l2 , _ = mp[q]
        # while l1 > l2:
        #     _, p = mp[p]
        #     l1 -= 1
        # while l2 > l1:
        #     _, q = mp[q]
        #     l2 -= 1
        # while p != q:
        #     _, p = mp[p]
        #     _, q = mp[q]
        # return p

        def rec(root, p, q):
            if root is None or root in [p,q]:
                return root
            left = rec(root.left, p, q)
            right = rec(root.right, p, q)
            if left and right:
                return root
            if left is None:
                return right
            if right is None:
                return left
        return rec(root, p, q)


        

        