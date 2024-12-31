class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])
        ans = 1
        prev = pairs[0][1]
        for x, y in pairs[1:]:
            if x > prev:
                prev = y
                ans += 1
        return ans
        