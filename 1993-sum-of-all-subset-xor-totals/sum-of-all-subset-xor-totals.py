class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        class Node:
            def __init__(self):
                self.children = {}
                self.end = 0

        root = Node()

        def build(index, curr):
            if index == len(nums):
                return

            for i in range(index, len(nums)):
                val = nums[i]

                if val not in curr.children:
                    curr.children[val] = Node()
                child = curr.children[val]
                child.end +=1

                build(i + 1, child)

        build(0, root)

        ans = 0

        def dfs(node, xor):
            nonlocal ans
            ans += (node.end * xor)

            for val, child in node.children.items():
                xor ^= val
                dfs(child, xor)
                xor ^= val

        dfs(root, 0)
        return ans