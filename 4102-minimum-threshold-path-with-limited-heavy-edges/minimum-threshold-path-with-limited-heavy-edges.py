class Solution:
    def minimumThreshold(self, n: int, edges: List[List[int]], source: int, target: int, k: int) -> int:
        
        if source == target:
            return 0
            
        mp = defaultdict(list)
        mini = 10 ** 10
        maxi = 0
        for x, y, w in edges:
            mp[x].append([y, w])
            mp[y].append([x, w])
            mini = min(mini, w)
            maxi = max(maxi, w)
        
        def check(val):
            queue = deque([source])
            dist = [float('inf')] * n
            dist[source] = 0
            while queue:
                node = queue.popleft()
                for neighbor, weight in mp[node]:
                    cost = 1 if weight > val else 0
                    if dist[node] + cost < dist[neighbor]:
                        dist[neighbor] = dist[node] + cost
                        if cost == 0:
                            queue.appendleft(neighbor)
                        else:
                            queue.append(neighbor)
            return dist[target]
        

        ans = -1
        lo, hi = 0, 10 ** 10
        while lo <= hi:
            mid = (lo + hi) // 2
            # print(check(mid), mid)
            if check(mid) <= k:
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return ans
        