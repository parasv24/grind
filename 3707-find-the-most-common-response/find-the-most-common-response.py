class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        mp = {}
        for day in responses:
            dmap = {}
            for one in day:
                dmap[one] = 1
            for key in dmap:
                mp[key] = mp.get(key, 0) + dmap[key]
        return sorted([[-1 * v, k] for k , v in mp.items()])[0][1]

        