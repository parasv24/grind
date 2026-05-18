class Solution:
    def minJumps(self, arr: List[int]) -> int:
        mp = defaultdict(list)
        for i in range(len(arr)):
            mp[arr[i]].append(i)
        queue = deque()
        vis = len(arr) * [0]
        queue.append([0, 0])
        vis[0] = 1
        steps = 0
        while queue:
            idx, steps = queue.popleft()
            if idx == len(arr) - 1:
                return steps
            if idx + 1 < len(arr) and vis[idx+1] == 0:
                queue.append([idx+1, steps+1])
                vis[idx+1] = 1
            if idx - 1 >=0 and vis[idx-1] == 0:
                queue.append([idx-1, steps+1])
                vis[idx-1] = 1
            
            for i in mp[arr[idx]]:
                if vis[i] == 0:
                    queue.append([i, steps+1])
                    vis[i] = 1
            mp[arr[idx]] = []
        return -1


        