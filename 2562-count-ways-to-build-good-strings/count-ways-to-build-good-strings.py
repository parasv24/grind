class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        @cache
        def helper(length):
            return (helper(length + zero) + helper(length + one) + int(low <= length <= high))% 1000000007 if length <= high else 0
        return helper(0)

        