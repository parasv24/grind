class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mp = Counter(nums)
        ans = 0
        for el in nums:
            if mp[el] > 0:
                cur = 1
                mp[el] = 0
                neg = el - 1
                pos = el + 1
                while(mp[neg] > 0):
                    mp[neg] = 0
                    cur += 1
                    neg -= 1
                while(mp[pos] > 0):
                    mp[pos] = 0
                    cur+= 1
                    pos+=1
                if cur > ans:
                    ans = cur
        return ans
        