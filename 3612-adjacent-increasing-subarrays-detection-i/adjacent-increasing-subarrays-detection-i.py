class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums) - (2 * k) + 1):
            is_i = True
            for j in range(i+1, i+k):
                if nums[j] <= nums[j-1]:
                    is_i = False
                    break
            if is_i:
                for j in range(i+k+1, i + k + k):
                    if nums[j] <= nums[j-1]:
                        is_i = False
                        break
            if is_i:
                return True
        return False

