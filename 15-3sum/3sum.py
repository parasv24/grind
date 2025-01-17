class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []


        for i in range(n-2):
            j = i + 1
            k = n - 1
            if i > 0 and nums[i] == nums[i-1]:
                continue

            while j < k:
                sm = nums[i] + nums[j] + nums[k]
                if sm > 0:
                    k -= 1
                elif sm < 0 :
                    j += 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    while j < k:
                        j += 1
                        if nums[j] != nums[j-1]:
                            break
                    while j < k:
                        k -= 1
                        if nums[k] != nums[k+1]:
                            break
        return res