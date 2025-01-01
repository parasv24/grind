class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        mp = {}
        for x, y, z in segments:
            mp[x] = mp.get(x, 0) + z      
            mp[y] = mp.get(y, 0) - z   
        res = []
        prev, color = None, 0
        for now in sorted(mp):
            if color:
                res.append((prev, now, color))
            color += mp[now]
            prev = now
        return res     