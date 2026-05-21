class Solution:
    def subsets(self, nums):
        class Node:
            def __init__(self):
                self.children = {}

        root = Node()

        def build(index, curr):
            if index == len(nums):
                return

            for i in range(index, len(nums)):
                val = nums[i]

                if val not in curr.children:
                    curr.children[val] = Node()

                build(i + 1, curr.children[val])

        build(0, root)

        ans = []

        def dfs(node, path):
            ans.append(path[:])

            for val, child in node.children.items():
                path.append(val)
                dfs(child, path)
                path.pop()

        dfs(root, [])
        return ans