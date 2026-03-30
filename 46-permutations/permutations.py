class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def rec(i):
            if i == len(nums) - 1:
                return[[nums[-1]]]
            small_ans = rec(i+1)
            ans = []
            for arr in small_ans:
                for idx in range(len(arr)+1):
                    prev = arr[0: idx] if idx > 0 else []
                    suf = arr[idx: ] if idx < len(arr) else []
                    ans.append([*prev, nums[i], *suf])
            return ans
        #return rec(0)

        ans = []
        def back(i):
            if i == len(nums):
                ans.append(nums[:])
                return
            for j in range(i, len(nums)):
                nums[i], nums[j] = nums[j], nums[i]
                back(i+1)
                nums[i], nums[j] = nums[j], nums[i]
            return
        back(0)
        return ans

                    


        