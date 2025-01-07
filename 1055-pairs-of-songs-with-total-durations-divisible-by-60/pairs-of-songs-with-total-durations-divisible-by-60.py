class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        mp = Counter()
        ans = 0
        for el in time:
            el %= 60
            if mp[(60 - el)%60] > 0:
                ans += mp[(60-el)%60]
                mp[el] += 1
            else:
                mp[el] += 1
        #print(mp)
        return ans
        