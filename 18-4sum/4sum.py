class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        ans = []
        nums.sort()
        for i in range(n-3):
            if i!= 0 and nums[i] == nums[i-1]:
                continue
            print("i", nums[i])
            for j in range(i+1, n-2):
                if j!= i+1 and nums[j] == nums[j-1]:
                    continue
                k = j + 1
                l = n - 1
                print("j", nums[j])
                total = target - nums[i] - nums[j]
                while k < l:
                    cur = nums[k] + nums[l]
                    if cur > total:
                        l -= 1
                    elif cur < total:
                        k +=1
                    else:
                        ans.append([nums[i], nums[j], nums[k], nums[l]])
                        k += 1
                        l -= 1
                        while k < l and nums[k] == nums[k-1]:
                            k += 1
                        while k < l and nums[l] == nums[l+1]:
                            l -=1
        return ans


        