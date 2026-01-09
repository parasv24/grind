class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mp = {}
        for el in nums:
            mp[el] = True
        ans = 0
        for key in mp.keys():
            if mp.get(key-1, False) == True:
                continue
            cur = 0
            # print(mp.get(key))
            while mp.get(key, False) == True:
                key += 1
                cur += 1
            if cur > ans:
                ans = cur
        return ans
            


