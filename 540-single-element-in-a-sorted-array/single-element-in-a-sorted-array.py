class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # approach 1 xor O(1)
        xor = 0
        for el in nums:
            xor ^= el
        return xor
        