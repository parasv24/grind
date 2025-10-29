class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev , idx = nums[0] , 1
        for el in nums[1:]:
            if el == prev:
                pass
            else:
                nums[idx] = el
                prev = el
                idx += 1
        return idx