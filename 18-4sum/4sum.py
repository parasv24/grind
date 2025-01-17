class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n-3):
            sm = nums[i]
                
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            for j in range(i+1, n-2):
                sm = nums[i] + nums[j]

                if j > i+1 and nums[j] == nums[j - 1]:
                    continue
                
                k = j + 1
                l = n - 1
                while k < l:
                    sm = nums[i] + nums[j]+ nums[k] + nums[l]
                    #print(i, j ,k ,l, sm)
                    if sm > target:
                        l -= 1
                    elif sm < target:
                        k += 1
                    else:
                        res.append([nums[i], nums[j], nums[k], nums[l]])
                        while k < l:
                            l -= 1
                            if nums[l] != nums[l+1]:
                                break
                        
                        while k < l:
                            k += 1
                            if nums[k] != nums[k-1]:
                                break
        return res