class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        def count_sort(exp):
            freq = [0] * 10
            for el in nums:
                freq[(el // exp) % 10] += 1
            
            for i in range(1, len(freq)):
                freq[i] += freq[i-1]

            arr = [0] * len(nums)
            for i in range(len(nums)-1, -1, -1):
                val = nums[i]
                digit = (val // exp) % 10
                arr[freq[digit] - 1] = val
                freq[digit] -= 1

            for i in range(len(nums)):
                nums[i] = arr[i]
        exp = 1
        mx = max(nums)
        while exp <= mx:
            count_sort(exp)
            exp = exp * 10
        
        ans = 0
        for i in range(1, len(nums)):
            ans = max(ans, nums[i] - nums[i-1])
        return ans