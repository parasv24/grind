class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ans = [-1] * len(nums)
        pos = 0
        neg = 0
        for el in nums:
            if el < 0:
                ans[2*neg + 1] = el
                neg += 1
            else:
                ans[2*pos] = el
                pos += 1
        return ans



            

        