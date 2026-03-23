class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stck = []
        for i in range(len(nums)-1, -1, -1):
            if len(stck) > 0:
                while len(stck) >0 and stck[-1] <= nums[i]:
                    stck.pop()
            stck.append(nums[i])

        ans = [-1 for _ in range(len(nums))]
        for i in range(len(nums)-1, -1, -1):
            if len(stck) > 0:
                while len(stck) >0 and stck[-1] <= nums[i]:
                    stck.pop()
                ans[i] = stck[-1] if len(stck) > 0 else -1
            stck.append(nums[i])
        return ans
        