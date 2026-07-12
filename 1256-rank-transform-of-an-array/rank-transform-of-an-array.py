class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        ans = [0] * len(arr)
        arr = [(el, idx) for idx, el in enumerate(arr)]
        arr.sort()
        prev = -10 ** 11
        rank = 0
        for el, idx in arr:
            if el != prev:
                rank += 1
            ans[idx] = rank
            prev = el
        return ans