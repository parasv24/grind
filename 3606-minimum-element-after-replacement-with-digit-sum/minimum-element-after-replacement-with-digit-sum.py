class Solution:
    def minElement(self, nums: List[int]) -> int:
        mini = 10000
        for el in nums:
            val = 0
            while el > 0:
                val += el % 10
                el = el // 10
            mini = min(val, mini)
        return mini
