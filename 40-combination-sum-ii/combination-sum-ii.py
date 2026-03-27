class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        def rec(i, arr, total, taken):
            if total > target:
                return
            if i == len(candidates):
                if total == target:
                    ans.append(arr)
                return
            
            rec(i+1, arr + [candidates[i]], total + candidates[i], 1)
            if i > 0 and candidates[i] == candidates[i-1] and taken == 1:
                return
            rec(i+1, arr, total, 0)
        rec(0, [], 0, 0)
        return ans
        