class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        mini, maxi = min(nums), max(nums)
        rangee = maxi - mini + 1
        freq = [0] * rangee
        for el in nums:
            freq[el - mini] += 1
        # print(freq)

        for i in range(1, len(freq)):
            freq[i] += freq[i-1]
        
        ans = [0] * len(nums)
        for i in range(len(nums)-1, -1, -1):
            val = nums[i]
            idx = freq[val - mini] - 1
            ans[idx] = val
            freq[val - mini] -= 1
        # print(freq)
        return ans
        