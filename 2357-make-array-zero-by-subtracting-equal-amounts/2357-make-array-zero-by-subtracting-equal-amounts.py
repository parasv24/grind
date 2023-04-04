class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums_set = set()
        for el in nums:
            if el!=0:
                nums_set.add(el)
        return len(nums_set)

        