class Solution:
    def evenSumSubgraphs(self, nums: list[int], edges: list[list[int]]) -> int:
        n = len(nums)
        arr = [(nums[i], i) for i in range(n)]
        def rec(i):
            if i == len(nums) - 1:
                return [[arr[i]]]
            small_ans = rec(i + 1)
            ans = []
            for val in small_ans:
                ans.append(val)
                ans.append(val + [arr[i]])
            ans.append([arr[i]])
            return ans
        sets = rec(0)
        valid_sets = []
        for inner_set in sets:
            val = 0
            for tup in inner_set:
                val += tup[0]
            if val % 2 == 0:
                valid_sets.append(inner_set)
        # print(valid_sets)
        ans = 0
        for inner_set in valid_sets:
            nodes = [tup[1] for tup in inner_set]
            # print(nodes)
            adj_list = defaultdict(list)
            for x, y in edges:
                if x in nodes and y in nodes:
                    adj_list[x].append(y)
                    adj_list[y].append(x)
            # print(adj_list)
            vis = {node: 0 for node in nodes}
            # print(vis)
            queue = deque()
            queue.append(nodes[0])
            vis[nodes[0]] = 1
            while len(queue) > 0:
                node = queue.popleft()
                for padosi in adj_list[node]:
                    if vis[padosi] == 0:
                        vis[padosi] = 1
                        queue.append(padosi)
            ans += int(sum(vis.values()) == len(nodes))
        return ans


        