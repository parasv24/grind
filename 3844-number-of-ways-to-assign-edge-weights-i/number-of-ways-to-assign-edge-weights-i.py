class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        mp = defaultdict(list)
        for x, y in edges:
            mp[x].append(y)
            mp[y].append(x)
        print(mp)

        def depth(root):
            queue = deque()
            queue.append([root, 0])
            vis = set()
            vis.add(root)
            dep = 0
            while queue:
                node, dep = queue.popleft()
                for child in mp[node]:
                    if child not in vis:
                        vis.add(child)
                        queue.append([child, dep + 1])
            return dep
        dep = depth(1)
        print(dep)
        MOD = 10 ** 9 + 7
        @cache
        def get_ways(n, val):
            if n == 0:
                return int(val == 1)
            return (get_ways(n-1, (val + 1) % 2) + get_ways(n-1, (val+2)%2)) % MOD
        
        # print(dep)
        return get_ways(dep, 0)
        