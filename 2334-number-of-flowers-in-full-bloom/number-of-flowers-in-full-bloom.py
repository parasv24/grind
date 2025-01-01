class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        mp = {}
        for x, y in flowers:
            mp[x] = mp.get(x, 0) + 1
            mp[y+1] = mp.get(y+1, 0) - 1
        for p in people:
            mp[p] = mp.get(p, 0) + 0

        prev = 0
        for k in sorted(mp.keys()):
            mp[k] += prev
            prev = mp[k]
        ans = []
        #print(mp)
        for p in people:
            ans.append(mp[p])
        return ans

        