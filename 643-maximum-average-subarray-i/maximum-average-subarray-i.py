class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sm = 0
        ans = -1000
        for i in range(len(nums)):
            if i <= k-1:
                sm += nums[i]
                if i == k-1:
                   ans = max(ans, sm/k) 
                   # print(i, ans)
            else:
                sm += nums[i]
                sm -= nums[i-k]
                ans = max(ans, sm/k)
                # print(i, ans)
        return ans

        