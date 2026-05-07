class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        def count_sort(idx, mp_idx):
            freq = [0] * 10
            for el in nums:
                digit = int(el[idx])
                freq[digit] += 1

            # print(idx, freq)
            for i in range(1, len(freq)):
                freq[i] += freq[i-1]
            
            ans = [0] * len(nums)
            # print(mp[mp_idx])
            for i in range(len(nums)-1, -1, -1):
                digit = int(mp[mp_idx][i][0][idx])
                index = freq[digit] - 1
                ans[index] = mp[mp_idx][i]
                freq[digit] -= 1
            
            return ans
            
        i = 1
        mp = {}
        mp[0] = [[nums[i], i] for i in range(len(nums))]
        mp_idx = 0
        while i <= len(nums[0]):
            mp[i] = count_sort(len(nums[0])-i, mp_idx)
            i += 1
            mp_idx += 1
        
        # print(mp)
        ans = []
        for k, trim in queries:
            ans.append(mp[trim][k-1][1])
        return ans
        