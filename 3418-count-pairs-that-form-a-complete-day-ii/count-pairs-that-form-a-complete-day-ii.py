class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        mp = Counter()
        ans = 0
        for el in hours:
            el %= 24
            if mp[(24 - el)%24] > 0:
                ans += mp[(24-el)%24]
                mp[el] += 1
            else:
                mp[el] += 1
        #print(mp)
        return ans
        