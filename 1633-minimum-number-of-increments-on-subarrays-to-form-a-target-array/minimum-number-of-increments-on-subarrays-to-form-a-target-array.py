class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        ans = 0
        prev = 0
        for el in target:
            if el > prev:
                ans += (el - prev)
            prev = el
        return ans        