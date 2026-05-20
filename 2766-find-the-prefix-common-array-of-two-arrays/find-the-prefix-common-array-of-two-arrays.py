class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        mp = {}
        ans = []
        prev = 0
        for x, y in zip(A, B):
            mp[x] = mp.get(x, 0) + 1
            mp[y] = mp.get(y, 0) - 1
            if mp[x] == 0:
                prev += 1
            if mp[y] == 0 and y!=x:
                prev += 1
            ans.append(prev)
        return ans
