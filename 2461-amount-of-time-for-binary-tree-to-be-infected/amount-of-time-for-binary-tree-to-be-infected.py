# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        graph = defaultdict(list)
        def dfs(root):
            if not root:
                return
            if root.left:
                graph[root.val].append(root.left.val)
                graph[root.left.val].append(root.val)
                dfs(root.left)
            if root.right:
                graph[root.val].append(root.right.val)
                graph[root.right.val].append(root.val)
                dfs(root.right)
        dfs(root)
        queue = deque()
        queue.append(start)
        vis = set()
        vis.add(start)
        t = -1
        while queue:
            for _ in range(len(queue)):
                front = queue.popleft()
                for adj in graph[front]:
                    if adj not in vis:
                        vis.add(adj)
                        queue.append(adj)
            t += 1
        return t


        