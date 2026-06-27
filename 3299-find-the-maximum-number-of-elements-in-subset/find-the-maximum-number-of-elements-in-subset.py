class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        nums.sort()
        ans = 0
        for el in nums:
            if cnt[el] > 0:
                start = el
                mini = 0
                while cnt[start] >= 2:
                    cnt[start] -= 2
                    mini += 2
                    start = start * start
                if cnt[start] == 0:
                    mini -= 1
                else:
                    mini += 1
                    cnt[start] -= 1
            ans = max(ans, mini)
        return ans
            
                    
                


