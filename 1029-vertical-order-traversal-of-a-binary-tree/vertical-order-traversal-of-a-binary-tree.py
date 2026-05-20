# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        ans = []
        mp = defaultdict(list)
        min_pos, max_pos = 0, 0
        queue.append([root, 0])
        while queue:
            level_mp = defaultdict(list)
            for _ in range(len(queue)):
                node, pos = queue.popleft()
                if pos < min_pos:
                    min_pos = pos
                if pos > max_pos:
                    max_pos = pos
                level_mp[pos].append(node.val)
                if node.left:
                    queue.append([node.left, pos - 1])
                if node.right:
                    queue.append([node.right, pos + 1])
            for key in level_mp:
                level_mp[key].sort()
                mp[key].extend(level_mp[key])
        for i in range(min_pos, max_pos+1):
            ans.append(mp[i])
        return ans
        