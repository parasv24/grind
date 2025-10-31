class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj , votes = -1, 0
        for el in nums:
            if votes == 0:
                maj = el
                votes = 1
            elif el == maj:
                votes += 1
            else:
                votes -= 1
        return maj