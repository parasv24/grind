class Solution:
    def centeredSubarrays(self, nums: List[int]) -> int:
        ans = len(nums)
        mp = {}
        mp[-1] = {}
        for idx, el in enumerate(nums):
            mp[idx] = mp[idx-1].copy()
            mp[idx][el] = mp[idx].get(el, 0) + 1
        p_sums = [0] + list(accumulate(nums))
        ans = 0
        for length in range(1, len(nums)+1):
            i = 0
            j = i + length - 1
            while j < len(nums):
                summ = p_sums[j+1] - p_sums[i]
                cnt1 = mp[j].get(summ, 0)
                cnt2 = mp[i-1].get(summ, 0)
                # print(i, j, cnt1, cnt2, summ)
                if cnt1 > cnt2:
                   ans += 1     
                i += 1
                j += 1
        return ans
            
            
                
        