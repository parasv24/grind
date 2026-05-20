class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        mask = 0
        ans = []
        prev = 0
        for x, y in zip(A, B):
            if mask & (1 << x):
                prev += 1
            else:
                mask = mask | (1 << x)
            if mask & (1 << y):
                prev += 1
            else:
                mask = mask | (1 << y)
            ans.append(prev)
        return ans
