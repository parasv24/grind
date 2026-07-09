class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        arr = [(nums[i], i) for i in range(n)]
        arr.sort()
        parent = list(range(n))
        rank = [0] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(u, v):
            pu, pv = find(u), find(v)
            ru, rv = rank[pu], rank[pv]

            if pu == pv:
                return
            
            if ru < rv:
                pu, pv = pv, pu
            
            parent[pv] = pu
            
            if ru == rv:
                rank[pu] += 1
            return
        
        for i in range(1, len(nums)):
            if abs(arr[i][0] - arr[i-1][0]) <= maxDiff:
                union(arr[i][1], arr[i-1][1])

        ans = []

        for x, y in queries:
            ans.append(find(x) == find(y))

        return ans 
            


        