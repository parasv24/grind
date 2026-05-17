class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        queue = deque()
        vis = set()
        queue.append(start)
        vis = [0] * len(arr)
        vis[start] = 1
        while queue:
            idx = queue.popleft()
            if arr[idx] == 0:
                return True
            
            for dx in [-arr[idx], arr[idx]]:
                if 0 <= idx + dx < len(arr) and vis[idx+dx] == 0:
                    queue.append(idx+dx)
                    vis[idx+dx] = 1
        return False
            
        