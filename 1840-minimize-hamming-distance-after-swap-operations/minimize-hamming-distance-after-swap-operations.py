class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        adj_list = defaultdict(list)
        for x, y in allowedSwaps:
            adj_list[x].append(y)
            adj_list[y].append(x)
        
        vis = [-1] * len(source)
        def dfs(i, mp):
            mp[source[i]] -= 1
            mp[target[i]] += 1
            for el in adj_list[i]:
                if vis[el] == -1:
                    vis[el] = 1
                    mp = dfs(el, mp)
            return mp
        
        ans = 0
        for i in range(len(source)):
            if vis[i] == -1:
                vis[i] = 1
                mp = dfs(i, defaultdict(int))
                print(mp)
                for k, v in mp.items():
                    if v > 0:
                        ans += v
        return ans
